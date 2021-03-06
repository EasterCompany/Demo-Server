# Django module imports
from django.db import models
from django.utils import timezone


class UserLogin(models.Model):
    uid = models.TextField(null=False, blank=False)
    email = models.TextField(null=False, blank=False)
    key = models.TextField(null=False, blank=False)
    gid = models.TextField(null=True, blank=True)
    fid = models.TextField(null=True, blank=True)
    dob = models.DateField(null=False, blank=False)
    date_joined = models.DateField(
        null=False, blank=False, default=timezone.now
    )
    last_active = models.DateField(
        null=False, blank=False, default=timezone.now
    )


class UserSessions(models.Model):
    uid = models.TextField(null=False, blank=False)
    key = models.TextField(null=False, blank=False)


class UserDetails(models.Model):
    uid = models.TextField(null=False, blank=False)
    display_image = models.TextField()
    display_name = models.TextField(null=False, blank=False)
    first_name = models.TextField()
    last_name = models.TextField()
