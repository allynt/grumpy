from django.contrib import admin

from grumpy.core.models import GrumpySettings


@admin.register(GrumpySettings)
class GrumpySettingsAdmin(admin.ModelAdmin):
    fields = (
        "allow_signin",
        "allow_signup",
        "require_verification",
        "password_min_length",
        "password_max_length",
        "password_strength",
        "max_free_books",
    )
