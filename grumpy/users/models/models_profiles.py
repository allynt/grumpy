from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

# UserProfile handles all app-related stuff


class UserProfile(models.Model):
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
        related_name="profile",
    )

    is_special = models.BooleanField(
        default=False,
        help_text=_("A special user can create and edit meetings."),
    )

    def __str__(self):
        return str(self.user)

    @property
    def can_add_books(self):
        return self.books.unread().count() < settings.MAX_FREE_BOOKS
