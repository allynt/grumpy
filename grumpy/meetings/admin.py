from dataclasses import dataclass

from django.contrib import admin
from django.contrib.gis import admin as gis_admin

from grumpy.meetings.models import Meeting


@dataclass
class Location:
    latitude: float
    longitude: float
    zoom: int = 12


DEFAULT_LOCATION = Location(50.618309, -3.410880)


@admin.register(Meeting)
class MeetingAdmin(gis_admin.GISModelAdmin):
    fields = (
        (
            "book",
            "date",
            "location",
            "notes",
        ),
    )
    list_display = (
        "date",
        "book",
    )

    gis_widget_kwargs = {
        "attrs": {
            "default_zoom": DEFAULT_LOCATION.zoom,
            "default_lat": DEFAULT_LOCATION.latitude,
            "default_lon": DEFAULT_LOCATION.longitude,
        },
    }
