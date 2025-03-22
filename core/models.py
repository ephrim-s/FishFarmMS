from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# These are the role options based on user type
ADMIN_ROLES = [('admin', 'Admin'), ('worker', 'Worker')]
USER_ROLES = [
    ('farmer', 'External Farmer'),
    ('wholesaler', 'Wholesaler'),
    ('retailer', 'Retailer'),
    ('consumer', 'Consumer'),
]

def get_user_roles(is_admin=False, for_registration=False):
    if for_registration:
        return USER_ROLES
    if is_admin:
        return ADMIN_ROLES + USER_ROLES
    return USER_ROLES

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email filed must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20,
        choices=get_user_roles(for_registration=True),  # Show only USER_ROLES for registration
        default='farmer'
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    geo_location = models.CharField(max_length=255, blank=True, null=True)
    customer_address = models.TextField(blank=True, null=True)
    destination_address = models.TextField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email} - {self.role}"
