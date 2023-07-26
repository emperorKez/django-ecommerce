from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.CharField(max_length=100, blank=False, null=False, unique=True)
    # username = models.CharField(max_length=50, null=True)
    # password1 = models.CharField(max_length=50, blank=False, null=False, unique=True)
    # password2 = models.CharField(max_length=50, blank=False, null=False, unique=True)
    # firstname = models.CharField(max_length=50, blank=False, null=False)
    # lastname = models.CharField(max_length=50, blank=False, null=False)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone_number = models.SmallIntegerField(blank=False, null=False)
    zip_code = models.CharField(max_length=100, blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    email_confirmed = models.BooleanField(default=False)
    is_subscribed = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    # REQUIRED_FIELDS = ['username', 'firstname', 'lastname', 'phone_number']
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email
