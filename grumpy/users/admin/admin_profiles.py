from django.contrib import admin
from django.db.models import F
from django.urls import resolve
from django.utils.translation import gettext_lazy as _

from grumpy.core.admin import (
    get_clickable_fk_for_list_display,
    CannotAddModelAdminBase,
    CannotDeleteModelAdminBase,
)

from grumpy.users.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(
    CannotAddModelAdminBase,
    # CannotDeleteModelAdminBase,  # (see `has_delete_permission` below)
    admin.ModelAdmin,
):
    actions = ("toggle_is_special",)
    list_display = (
        "get_name_for_list_display",
        "get_user_for_list_display",
        "is_special",
    )
    list_filter = ("is_special",)
    readonly_fields = ("user",)
    search_fields = ("user__email",)

    @admin.display(description="PROFILE")
    def get_name_for_list_display(self, obj):
        return str(obj)

    @admin.display(description="USER")
    def get_user_for_list_display(self, obj):
        return get_clickable_fk_for_list_display(obj.user)

    def has_delete_permission(self, request, obj=None):
        """
        UserProfiles can be deleted in response to deleting a User from
        the UserAdmin.  But not directly from the UserProfileAdmin.
        """
        view_name = resolve(request.path).view_name
        return view_name in [
            "admin:users_user_changelist",
            "admin:users_user_change",
            "admin:users_user_delete",
        ]

    @admin.display(description=_("Toggle specialness of selected Users"))
    def toggle_is_special(self, request, queryset):
        queryset.update(is_special=~F("is_special"))
