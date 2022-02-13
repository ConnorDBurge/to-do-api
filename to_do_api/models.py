from django.db import models
from django.contrib.auth.models import AbstractBaseUser 
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings # settings from to_do_proj/settings.py


class UserProfileManager(BaseUserManager):
    
    # override stock create_user() method from Django
    def create_user(self, email, first_name, last_name, password=None):
        """Create a new user"""
        if not email: raise ValueError('You must provide an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password) # hash password
        user.save(using=self._db)
        return user
    
    # override stock create_user() method from Django
    def create_superuser(self, email, first_name, last_name, password):
        """Create a new superuser"""
        user = self.create_user(email, first_name, last_name, password)
        user.is_superuser = True # is_superuser auto created
        user.is_staff = True # is_staff auto created
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin): # inherits from the basic Django User model

    email = models.EmailField(max_length=255, unique=True) # must be unique in DB
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email' # auto required 
    REQUIRED_FIELDS = ['first_name', 'last_name'] # add to required fields
    
    def get_full_name(self):
        """Retrieve the full name of the user"""
        return f'{self.first_name} {self.last_name}'
    
    def get_first_name(self):
        """Retrieve the first name of the user"""
        return self.first_name
    
    def __str__(self):
        """Return a string representation"""
        return self.email
    
class ToDoItem(models.Model):
    """User To-Do item"""
    user_profile = models.ForeignKey( # User that creates this item
        settings.AUTH_USER_MODEL, # set in to_do_proj/settings.py
        on_delete=models.CASCADE
    )
    task = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.status_text