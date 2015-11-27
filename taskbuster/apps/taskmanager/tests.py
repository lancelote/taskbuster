# coding=utf-8

from django.contrib.auth import get_user_model
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
