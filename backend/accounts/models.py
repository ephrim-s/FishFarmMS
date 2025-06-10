from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=[
        ('admin', 'Admin'),
        ('worker', 'Worker'),
        ('farmer', 'External Farmer'),
        ('wholesaler', 'Wholesaler'),
        ('retailer', 'Retailer'),
        ('consumer', 'Consumer'),
    ], default='farmer')
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)