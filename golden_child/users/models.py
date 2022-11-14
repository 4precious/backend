from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        if not password:
            raise ValueError('Users require a password field')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
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


USERTYPE = (
    ('PARENT', 'Parent'),
    ('CHILD', 'Child')
)


class User(AbstractUser):
    user_type = models.CharField(max_length=10, choices=USERTYPE)
    # is_parent = models.BooleanField(default=False)
    # is_child = models.BooleanField(default=False)
    username = None
    email = models.EmailField(_('email address'), unique=True)
    linked_user = models.EmailField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def get_usertype(self):
        return self.user_type

    # def get_isparent(self):
    #     return self.is_parent

    # def get_ischild(self):
    #     return self.is_child

    def __str__(self):
        return self.email
