import uuid
from dataclasses import dataclass

from django.contrib.gis.db import models as gis_models
from django.db import models
from django.db.models.functions import Now

from grumpy.books.models import Book


@dataclass
class Location:
    latitude: float
    longitude: float
    zoom: int = 12


DEFAULT_LOCATION = Location(50.618309, -3.410880)


MODEL_DATETIME_FORMAT_CODE = "%d %B %Y @ %I:%M"


class MeetingManager(models.Manager):
    pass


class MeetingQuerySet(models.QuerySet):

    def future(self):
        return self.filter(status=Meeting.MeetingStatus.FUTURE)

    def past(self):
        return self.filter(status=Meeting.MeetingStatus.PAST)


class Meeting(gis_models.Model):

    class Meta:
        verbose_name = "Meeting"
        verbose_name_plural = "Meetings"
        ordering = ["-date"]

    objects = MeetingManager.from_queryset(MeetingQuerySet)()

    class MeetingStatus(models.TextChoices):
        PAST = "PAST", "Past"
        FUTURE = "FUTURE", "Future"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    date = models.DateTimeField(db_default=Now())
    location = gis_models.PointField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    status = models.CharField(
        max_length=16, choices=MeetingStatus.choices, default=MeetingStatus.FUTURE
    )

    book = models.OneToOneField(
        Book, blank=False, null=False, related_name="meeting", on_delete=models.PROTECT
    )

    def __str__(self):
        datetime_format_string = self.date.strftime(MODEL_DATETIME_FORMAT_CODE)
        return f'{datetime_format_string} - "{self.book}"'
