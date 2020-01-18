from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import JSONField

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)
    password = models.CharField(max_length = 100)
    balance = JSONField(null = True)
    is_superuser = models.BooleanField(default = False)
    created_date = models.DateTimeField(auto_now_add = True)
    iban = models.CharField(max_length = 50, null = True)
    
    def __str__(self):
        return self.email