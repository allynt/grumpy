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
            "title",
            "author",
            "description",
        ),
    )
    readonly_fields = ("id",)
    list_display = ("id",)
