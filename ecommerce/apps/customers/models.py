from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, commit=True):

        if not email:
            raise ValueError(_('Users must have an email address'))
        if not name:
            raise ValueError(_('Users must have a username'))

        user = self.model(email=self.normalize_email(email), name=name)

        user.set_password(password)
        if commit:
            user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):

        user = self.create_user(
            email,
            password=password,
            name=name,
            commit=False,
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class Customer(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = "customer"
        ordering = ['-created_at']
    
    email = models.EmailField(
        verbose_name=_('email'),
        max_length=255,
        unique=True
    )

    name = models.CharField(
        verbose_name=_('customer name'),
        max_length=50,
        blank=True
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
    )

    is_staff = models.BooleanField(
        _('staff'),
        default=False
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    created_at = models.DateTimeField(
        verbose_name=_('created_at'),
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name=_('updated_at'),
        auto_now=True
    )

    def __str__(self):
        return '{} <{}>'.format(self.email, self.name)
