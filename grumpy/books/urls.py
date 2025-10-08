from django.urls import path

from grumpy.books.views import (
    BookListView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path("", BookListView.as_view(), name="book-list"),
    path("add/", BookCreateView.as_view(), name="book-add"),
    path("<uuid:pk>/", BookUpdateView.as_view(), name="book-update"),
    path("<uuid:pk>/delete/", BookDeleteView.as_view(), name="book-delete"),
]
