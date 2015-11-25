# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils.translation import activate


class TestGoogleLogin(StaticLiveServerTestCase):

    fixtures = ['allauth_fixture']

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.browser.wait = WebDriverWait(self.browser, 10)
        activate('en')

    def tearDown(self):
        self.browser.quit()

    def get_element_by_id(self, element_id):
        return self.browser.wait.until(
            expected_conditions.presence_of_element_located(
                (By.ID, element_id)
            )
        )

    def get_button_by_id(self, button_id):
        return self.browser.wait.until(
            expected_conditions.element_to_be_clickable(
                (By.ID, button_id)
            )
        )

    def get_element_by_css_selector(self, css_selector):
        return self.browser.wait.until(
            expected_conditions.element_to_be_clickable(
                (By.CSS_SELECTOR, css_selector)
            )
        )

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def user_login(self):
        import json
        with open('taskbuster/fixtures/google_user.json') as f:
            credentials = json.loads(f.read())
        self.get_element_by_id('Email').send_keys(credentials['Email'])
        self.get_button_by_id('next').click()
        self.get_element_by_id('Passwd').send_keys(credentials['Passwd'])
        for btn in ['signIn', 'submit_approve_access']:
            self.get_button_by_id(btn).click()

    def test_google_login(self):
        self.browser.get(self.get_full_url('home'))
        google_login = self.get_element_by_id('google_login')
        with self.assertRaises(TimeoutException):
            self.get_element_by_id('logout')
        self.assertEqual(
            google_login.get_attribute('href'),
            self.live_server_url + '/accounts/google/login'
        )
        google_login.click()
        self.user_login()
        with self.assertRaises(TimeoutException):
            self.get_element_by_id('google_login')
        google_logout = self.get_element_by_id('logout')
        google_logout.click()
        logout_confirmation = self.get_element_by_css_selector('form button')
        logout_confirmation.click()
        google_login = self.get_element_by_id('google_login')
