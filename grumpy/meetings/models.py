import uuid

from django.contrib.gis.db import models as gis_models
from django.db import models
from django.db.models.functions import Now

from grumpy.books.models import Book

DATETIME_FORMAT_CODE = "%d %B %Y @ %I:%M"


class MeetingManager(models.Manager):
    pass


class MeetingQuerySet(models.QuerySet):
    # TODO: future/past
    pass


class Meeting(gis_models.Model):

    class Meta:
        verbose_name = "Meeting"
        verbose_name_plural = "Meetings"
        ordering = ["-date"]

    objects = MeetingManager.from_queryset(MeetingQuerySet)

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    date = models.DateTimeField(db_default=Now())
    location = gis_models.PointField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    # status: enum FUTURE, PAST

    book = models.OneToOneField(
        Book, blank=False, null=False, related_name="meeting", on_delete=models.PROTECT
    )

    def __str__(self):
        datetime_format_string = self.date.strftime(DATETIME_FORMAT_CODE)
        return f'{datetime_format_string} - "{self.book}"'
