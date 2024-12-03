from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Additional fields for Google Auth
    google_id = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.URLField(max_length=1024, null=True, blank=True)
    
    # We'll keep the following fields from AbstractUser:
    # - username
    # - email
    # - first_name
    # - last_name
    # - password (handled by Django)
    # - is_active
    # - date_joined

    class Meta:
        db_table = 'auth_user'
