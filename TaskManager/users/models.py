from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):
    ROLES_CHOICES=(
        ('admin','Admin'),
        ('manager','Manager'),
        ('member','Member'),
    )
    role=models.CharField(max_length=20, choices=ROLES_CHOICES, default='member')