import uuid

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from core.abstract.models import AbstractModel, AbstractManager
from django.http import Http404


def user_directory_path(instance, filename):
    return f"user_{instance.user.id}/{filename}"


# Create your models here.
class UserManager(BaseUserManager, AbstractManager):
    def create_user(self, username, email, password=None, **kwargs):
        """Create and return a `User` object with an email, phone_number, username
        and password."""
        if username is None:
            raise TypeError("Users must have a username")
        if email is None:
            raise TypeError("Users must have an email")
        if password is None:
            raise TypeError('Users must have password')

        user = self.model(username=username,
                          email=self.normalize_email(email),
                          **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password, **kwargs):
        """Create and return a `User` with admin privileges"""
        if username is None:
            raise TypeError("Superusers must have a username")
        if email is None:
            raise TypeError("Superusers must have an email")
        if password is None:
            raise TypeError('Superusers must have password')
        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, blank=True, upload_to=user_directory_path)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def name(self):
        return f"{self.last_name} {self.first_name}"
