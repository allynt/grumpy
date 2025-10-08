import uuid

from enum import Enum

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.functions import Lower
from django.urls import reverse

from grumpy.users.models import UserProfile


class BookStatus(str, Enum):

    UNREAD = "Unread"
    READ = "Read"
    READING = "Reading"


class BookManager(models.Manager):
    def get_by_natural_key(self, title, author):
        return self.get(title=title, author=author)


class BookQuerySet(models.QuerySet):

    def read(self):
        return self.filter(meeting__isnull=False)

    def unread(self):
        return self.filter(meeting__isnull=True)


class Book(models.Model):

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        constraints = [
            models.UniqueConstraint(
                Lower("title").desc(),
                Lower("author").desc(),
                name="unique_title_author",
                violation_error_message="A book with the same title/author combination exists.",
            )
        ]

    objects = BookManager.from_queryset(BookQuerySet)()

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    title = models.CharField(max_length=255, blank=False, null=False)
    author = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)

    owner = models.ForeignKey(
        UserProfile,
        blank=True,
        null=True,
        related_name="books",
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book-update", kwargs={"pk": self.pk})

    def natural_key(self):
        return (
            self.title,
            self.author,
        )

    @property
    def status(self):
        try:
            meeting = self.meeting
            # TODO: A BIT MORE FINE-GRAINED
            return BookStatus.READ
        except ObjectDoesNotExist:
            return BookStatus.UNREAD
