from django.contrib import admin

from grumpy.meetings.models import Meeting


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    fields = (
        (
            "book",
            "date",
            "notes",
        ),
    )
    list_display = (
        "date",
        "book",
    )
