import logging

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)
from django.contrib.auth.base_user import BaseUserManager
from django.db.models import Q

logger = logging.getLogger(__name__)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(email=self.normalize_email(email), 
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(email, password, **extra_fields)
    
    def get_by_natural_key(self, username: str | None):
        """
        Retrieves a User object by its natural key, which is its email address.

        Args:
            username (str | None): The email address of the user to retrieve.

        Returns:
            User | None: The User object with the given email address, or None if no such user exists.
        """
        return self.get(Q(email__iexact=username))

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email',
                              max_length=255, unique=True,
                              error_messages={'unique': 'Sorry, this email is already in use.'})
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name')

    objects = UserManager()

    def get_gull_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.email
    
    def has_perm(self, perm, obj=None) -> bool:
        return True

    def has_module_perms(self, app_label):  # pragma: no cover
        """
        Check if the user has privileges to the given app.

        :param app_label: The label of the app on which to check for permissions.
        :return: True if the user has privileges for app, False otherwise
        """
        return True
    
    @admin.display(
        boolean=False,
        ordering="email",
        description="Sorted by email",
    )
    def get_email_sorted_display(self):
        return self.email
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'