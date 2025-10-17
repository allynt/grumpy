from django.contrib import admin

from grumpy.books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    exclude = [
        "owner",
    ]  # IMPORTANT: KEEP THIS HIDDEN TO RETAIN ANONYMITY
    fields = (
        (
            "id",
            "created_at",
            "updated_at",
            "title",
            "author",
            "description",
        ),
    )
    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )
    list_display = (
        "id",
        "created_at",
    )
