from django.contrib import admin

from grumpy.books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    exclude = [
        "owner",
    ]  # IMPORTANT: KEEP THIS HIDDEN TO RETAIN ANONYMITY
    fields = (
        (
            "title",
            "author",
            "description",
        ),
    )
    list_display = (
        "title",
        "author",
    )
