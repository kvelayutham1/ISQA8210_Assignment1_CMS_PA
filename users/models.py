from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    department = models.CharField(max_length=50, default='', null=True, blank=True)
    employee_cell_phone = models.CharField(max_length=50, default='', null=True, blank=True)
    