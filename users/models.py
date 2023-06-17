from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User must have an email!")
        if not username:
            raise ValueError("User must have a username!")
        if not password:
            raise ValueError("User must have a password!")

        # Create instance of the user class using self inheritance
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        su = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )

        su.is_staff     = True
        su.is_admin     = True
        su.is_superuser = True

        su.save(using=self._db)
        return su


class User(AbstractBaseUser):
    email           = models.EmailField(unique=True)
    username        = models.CharField(unique=True, max_length=64)

    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
