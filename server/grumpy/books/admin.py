from django.contrib import admin

from grumpy.books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = (
        (
            "title",
            "author",
            "description",
            "owner",  # TODO: REMOVE THIS
        ),
    )
    list_display = (
        "title",
        "author",
    )
