from __future__ import unicode_literals

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.
from django.utils import timezone

import settings
from constants import USER_STATUS_CHOICES, active, GENDER_CHOICES, Other
from django.contrib.auth.models import User

class User_Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    username = models.CharField(max_length=64, null=True)
    city = models.CharField(max_length=32, null=True, default='chaoyang')
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES,
                              default=Other, null=True)
    bio = models.CharField(max_length=1024, null=True, blank=True)
    avatar = models.CharField(max_length=255, null=True)
    email_verified = models.BooleanField(default=False)
    update_time = models.DateTimeField(default=timezone.now, null=True)

    @property
    def avatar_url(self):
        if not self.avatar:
            return "%s%s" % (settings.STATIC_URL, 'images/avatar/man.png')
        if 'http' in self.avatar:
            return self.avatar
        # elif self.avatar:
        #     return "%s%s" % (avatar_host, self.avatar)
        else:
            if self.gender == 'W':
                return "%s%s" % (settings.STATIC_URL, 'images/avatar/woman.png')
            return "%s%s" % (settings.STATIC_URL, 'images/avatar/man.png')

    class Meta:
        db_table = 'user_profile'
        ordering = ['-update_time']