from django.db import models
from django.utils import timezone


class APIUser(models.Model):
    username = models.CharField(max_length=50,unique=True,blank=False,null=False)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    votes = models.IntegerField()
