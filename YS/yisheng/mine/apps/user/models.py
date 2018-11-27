from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=11, verbose_name='手机', default='', null=True, blank=True)
    qq = models.CharField(max_length=30, verbose_name='QQ', default='', null=True, blank=True)

    def __str__(self):
        return self.username

    # ChoicesField = {}