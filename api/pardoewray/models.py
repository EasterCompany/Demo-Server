# Django module imports
from django.db import models
from django.utils import timezone


class Jobs(models.Model):

    class Meta:
        ordering= ['-id']

    uid = models.TextField(null=False, blank=False, unique=True)
    Title = models.TextField(null=False, blank=False)
    Company = models.TextField(null=False, blank=False)
    Website = models.TextField(default="")
    Location = models.TextField(default="")
    Type = models.TextField(null=False, blank=False, default="Permanent")
    Description = models.TextField(null=False, blank=False, default="")
    Date_Added = models.DateField(
        null=False, blank=False, default=timezone.now
    )


class JobRequirements(models.Model):
    uid = models.TextField(null=False, blank=False)
    required = models.TextField(null=False, blank=False)


class NewsLetter(models.Model):
    Title = models.TextField(null=False, blank=False)
    Content = models.TextField(null=False, blank=False)
    Date_Added = models.DateField(
        null=False, blank=False, default=timezone.now
    )
