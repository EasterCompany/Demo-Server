# Standard library imports
from datetime import datetime, timedelta
# Django module imports
from django.db import models
from django.utils import timezone


def session_expire_date():
    return (datetime.now() + timedelta(days=1)).strftime("%Y/%m/%d %H:%M:%S")


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
    expires = models.DateField(
        null=False, blank=False, default=session_expire_date
    )
