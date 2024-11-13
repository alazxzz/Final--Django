from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    roles = models.ManyToManyField(Role)
    last_login = models.DateTimeField(auto_now=True)