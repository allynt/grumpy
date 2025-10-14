from django.contrib import admin

from grumpy.core.models import GrumpySettings


@admin.register(GrumpySettings)
class GrumpySettingsAdmin(admin.ModelAdmin):
    fields = (
        "allow_signin",
        "allow_signup",
        "require_approval",
        "notify_signups",
        "password_min_length",
        "password_max_length",
        "password_strength",
        "max_free_books",
    )
