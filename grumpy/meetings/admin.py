from dataclasses import dataclass

from django.contrib import admin
from django.contrib.gis import admin as gis_admin

from grumpy.meetings.models import Meeting, DEFAULT_LOCATION


@admin.register(Meeting)
class MeetingAdmin(gis_admin.GISModelAdmin):
    fields = (
        (
            "id",
            "book",
            "date",
            "status",
            "location",
            "notes",
        ),
    )
    list_display = (
        "date",
        "book",
        "status",
    )
    list_filter = ("status",)
    readonly_fields = ("id",)

    gis_widget_kwargs = {
        "attrs": {
            "default_zoom": DEFAULT_LOCATION.zoom,
            "default_lat": DEFAULT_LOCATION.latitude,
            "default_lon": DEFAULT_LOCATION.longitude,
        },
    }
