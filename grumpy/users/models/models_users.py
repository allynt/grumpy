import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

########################
# managers & querysets #
########################


class UserManager(BaseUserManager):
    """
    A custom manager that ignores username in favor of email
    """

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        if not email:
            raise ValueError("User must have an email")

        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class UserQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)

    def inactive(self):
        return self.filter(is_active=False)


class User(AbstractUser):
    """
    Grumpy User
    """

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    objects = UserManager.from_queryset(UserQuerySet)()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    # disable some of the built-in fields...
    username = None
    first_name = None
    last_name = None

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    email = models.EmailField(
        # b/c email is used as the identifying field,
        # it is redefined here as required and unique
        _("email address"),
        blank=False,
        unique=True,
        error_messages={
            "unique": _("A user with that email address already exists."),
        },
    )

    verified = models.BooleanField(
        default=False, help_text=_("Has this user been verified?")
    )

    def __str__(self):
        return self.email
