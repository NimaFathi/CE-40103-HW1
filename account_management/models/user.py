from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from simple_history.models import HistoricalRecords

from _helpers.db import TimeModel


class MyAccountManager(BaseUserManager):

    def create_user(self, name, username, password=None):
        if not name:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("User must have an username")
        user = self.model(
            name=name,
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, name, username, password):
        user = self.create_user(
            name=name,
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, TimeModel):
    history = HistoricalRecords()
    name = models.CharField(max_length=30, null=False)
    username = models.CharField(max_length=30, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']
    objects = MyAccountManager()

    def __str__(self):
        return self.username

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = 'اکانت'
        verbose_name_plural = 'اکانت‌ها'
