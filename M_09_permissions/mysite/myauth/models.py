from __future__ import unicode_literals
from django.db.models import (
    BooleanField, EmailField, CharField, DateTimeField, TextField
)
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = EmailField(_('email'), unique=True)
    first_name = CharField(_('name'), max_length=30, blank=True)
    last_name = CharField(_('surname'), max_length=30, blank=True)
    agreement_accepted = BooleanField(default=False)
    date_joined = DateTimeField(_('registered'), auto_now_add=True)
    is_active = BooleanField(_('is_active'), default=True)
    biography = TextField(max_length=500, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns first_name and last_name with a space between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns short form of the user's name.
        """
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to the user.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

