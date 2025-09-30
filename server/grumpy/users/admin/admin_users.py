from django.contrib import admin
from django.contrib import messages
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _

from grumpy.users.models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    model = User
    actions = "toggle_email"
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "verified",
                ),
            },
        ),
    )
    fieldsets = (
        (None, {"fields": ("id", "email", "password")}),
        (
            _("General info"),
            {"fields": ("verified",)},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = (
        "email",
        "is_staff",
        "is_active",
        "verified",
    )
    list_filter = (
        "is_staff",
        "is_active",
        "verified",
    )
    readonly_fields = ("id",)
    search_fields = ("email",)
    ordering = ("email",)

    @admin.display(description=_("Toggle verification of selected Users"))
    def toggle_verified_email(self, request, queryset):
        # doing this cleverly w/ negated F expressions is not supported
        # (as per: https://code.djangoproject.com/ticket/17186)
        # queryset.update(verified=not(F("verified")))
        for obj in queryset:
            obj.verified = not obj.verified
            obj.save()

            msg = (
                f"{obj} {'has not' if not obj.verified_email else 'has'} been verified."
            )
            self.message_user(request, msg)
