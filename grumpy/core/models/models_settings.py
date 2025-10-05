from datetime import timedelta

from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from grumpy.core.mixins import SingletonMixin


class GrumpySettings(SingletonMixin, models.Model):
    class Meta:
        verbose_name = "Settings"
        verbose_name_plural = "Settings"

    allow_signin = models.BooleanField(
        default=True,
        help_text=_("Allow users to signin."),
    )

    allow_signup = models.BooleanField(
        default=True,
        help_text=_("Allow users to register."),
    )

    require_approval = models.BooleanField(
        default=False,
        help_text=_("Require a user to be manually approved."),
    )

    password_min_length = models.PositiveIntegerField(
        default=6, help_text=_("Minimum length of a user password")
    )
    password_max_length = models.PositiveIntegerField(
        default=255, help_text=_("Maximum length of a user password")
    )

    password_strength = models.IntegerField(
        default=2,
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        help_text=_(
            "Strength of password field as per <a href='github.com/dropbox/zxcvbn'>zxcvbn</a>"
        ),
    )

    max_free_books = models.PositiveIntegerField(
        default=2, help_text=_("Number of unread books a user can own.")
    )

    def clean(self, *args, **kwargs):
        if self.password_max_length <= self.password_min_length:
            raise ValidationError(
                _("password_max_length must be greater than password_min_length")
            )

    def __str__(self):
        return "Grumpy Settings"
