# coding=utf-8

from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy

from . import managers


class Profile(models.Model):

    # Relations
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='profile',
        verbose_name=ugettext_lazy('user')
    )

    # Attributes - Mandatory
    interaction = models.PositiveIntegerField(
        default=0,
        verbose_name=ugettext_lazy('interaction')
    )

    # Attributes - Optional
    # Object Manager
    objects = managers.ProfileManager()

    # Custom Properties
    @property
    def username(self):
        return self.user.username

    # Methods
    # Meta and String
    class Meta:
        verbose_name = ugettext_lazy('Profile')
        verbose_name_plural = ugettext_lazy('Profiles')
        ordering = ('user',)

    def __str__(self):
        return self.user.username


class Project(models.Model):

    # Relations
    user = models.ForeignKey(
        Profile,
        related_name='projects',
        verbose_name=ugettext_lazy('user')
    )

    # Attributes - Mandatory
    name = models.CharField(
        max_length=100,
        verbose_name=ugettext_lazy('name'),
        help_text=ugettext_lazy('Enter the project name')
    )
    color = models.CharField(
        max_length=7,
        default='#fff',
        validators=[RegexValidator(r'(^#[0-9a-fA-F]{3}$)|(^#[0-9a-fA-F]{6}$)')],
        verbose_name=ugettext_lazy('color'),
        help_text=ugettext_lazy(
            'Enter the hex color code, like #ccc or #cccccc'
        )
    )

    # Attributes - Optional
    # Object Manager
    objects = managers.ProjectManager()

    # Custom Properties
    # Methods

    # Meta and String
    class Meta:
        verbose_name = ugettext_lazy('Project')
        verbose_name_plural = ugettext_lazy('Projects')
        ordering = ('user', 'name')
        unique_together = ('user', 'name')

    def __str__(self):
        return '%s - %s' % (self.user, self.name)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_for_new_user(sender, created, instance, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()
