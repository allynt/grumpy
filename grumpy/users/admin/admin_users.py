from django.contrib import admin
from django.contrib import messages
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _

from grumpy.users.models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    model = User
    actions = ("toggle_approval",)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_approved",
                ),
            },
        ),
    )
    fieldsets = (
        (None, {"fields": ("id", "email", "password")}),
        (
            _("General info"),
            {"fields": ("is_approved",)},
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
        "is_approved",
    )
    list_filter = (
        "is_staff",
        "is_active",
        "is_approved",
    )
    readonly_fields = ("id",)
    search_fields = ("email",)
    ordering = ("email",)

    @admin.display(description=_("Toggle approval of selected Users"))
    def toggle_approval(self, request, queryset):
        # TODO: doing this cleverly w/ negated F expressions is not supported
        # (as per: https://code.djangoproject.com/ticket/16211)
        # queryset.update(is_approved=~F("is_approved"))
        for obj in queryset:
            obj.is_approved = not obj.is_approved
            obj.save()

            msg = f"{obj} {'not' if not obj.is_approved else ''} approved."
            self.message_user(request, msg)
