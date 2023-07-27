from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from shortuuid.django_fields import ShortUUIDField

class User(AbstractUser):
    user_id = ShortUUIDField(unique=True, default=uuid4, editable=False, length= 10, alphabet='1234567890')
    email = models.CharField(max_length=100, blank=False, null=False, unique=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50, verbose_name='Last Name')
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone_number = models.SmallIntegerField(blank=True, null=True)
    zip_code = models.CharField(max_length=100, blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    email_confirmed = models.BooleanField(default=False)
    is_subscribed = models.BooleanField(default=True)
    is_vendor = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    first_name = 'firstname'
    last_name = 'lastname'
    # REQUIRED_FIELDS = ['username', 'firstname', 'lastname', 'phone_number']
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email
