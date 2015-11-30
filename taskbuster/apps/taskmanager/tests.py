# coding=utf-8

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from . import models


class TestProfileModel(TestCase):

    def test_profile_creation(self):
        User = get_user_model()

        # New user created
        user = User.objects.create(
            username='taskbuster', password='django_tutorial'
        )

        # Check that a Profile instance has been created
        self.assertIsInstance(user.profile, models.Profile)

        # Call the save method of the user to activate the signal again, and
        # check that it doesn't try to create another profile instance
        user.save()
        self.assertIsInstance(user.profile, models.Profile)


class TestProjectModel(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create(
            username='taskbuster', password='django-tutorial'
        )
        self.profile = self.user.profile

    def tearDown(self):
        self.user.delete()

    def test_color_validation(self):
        # This first project uses the default value of #fff
        project = models.Project(
            user=self.profile,
            name='TackManager'
        )
        self.assertTrue(project.color, '#fff')

        # Validation should not raise an error
        project.full_clean()

        # Good color inputs (without errors)
        for color in ['#1cA', '#1256aB']:
            project.color = color
            project.full_clean()

        # Bad color inputs
        for color in [
            "1cA", "1256aB", "#1", "#12", "#1234", "#12345", "#1234567"
        ]:
            with self.assertRaises(ValidationError):
                project.color = color
                project.full_clean()
