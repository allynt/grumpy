from django.db import models
from django.db.models.functions import Now

from grumpy.books.models import Book

DATE_FORMAT_CODE = "%d %B %Y @ %I:%M"


class MeetingManager(models.Manager):
    pass


class MeetingQuerySet(models.QuerySet):
    # TODO: future/past
    pass


class Meeting(models.Model):

    class Meta:
        verbose_name = "Meeting"
        verbose_name_plural = "Meetings"

    objects = MeetingManager.from_queryset(MeetingQuerySet)

    date = models.DateTimeField(db_default=Now())
    # location = models.CharField(max_length=255, blank=False, null=False)
    notes = models.TextField(blank=True, null=True)
    # status: enum FUTURE, PAST

    book = models.OneToOneField(
        Book, blank=False, null=False, related_name="meeting", on_delete=models.PROTECT
    )

    def __str__(self):
        datetime_format_string = self.date.strftime(DATE_FORMAT_CODE)
        return f'{datetime_format_string} - "{self.book}"'
