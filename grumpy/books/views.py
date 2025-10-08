import logging

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from grumpy.books.models import Book

logger = logging.getLogger(__name__)


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    fields = [
        "title",
        "author",
        "description",
    ]
    context_object_name = "books"
    template_name = "books/book_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        context["profile"] = current_user.profile
        return context

    def get_queryset(self):
        current_user = self.request.user
        queryset = Book.objects.filter(owner=current_user.profile)
        return queryset


class BookCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Book
    fields = [
        "title",
        "author",
        "description",
    ]
    template_name = "books/book_form.html"
    success_url = reverse_lazy("book-list")

    def form_valid(self, form):
        current_user = self.request.user
        form.instance.owner = current_user.profile
        return super().form_valid(form)

    def test_func(self):
        # fn to use w/ https://docs.djangoproject.com/en/5.2/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin
        current_user = self.request.user
        user_can_add_books = current_user.profile.can_add_books
        if not user_can_add_books:
            logger.error(f"PermissionDeniedError: {current_user} cannot add books.")
        return user_can_add_books


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = [
        "title",
        "author",
        "description",
    ]
    template_name = "books/book_form.html"
    context_object_name = "book"

    def test_func(self):
        # fn to use w/ https://docs.djangoproject.com/en/5.2/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin
        current_user = self.request.user
        current_object = self.get_object()
        user_can_update_book = current_object.owner == current_user.profile
        if not user_can_update_book:
            logger.error(
                f"PermissionDeniedError: {current_user} cannot update {current_object}."
            )
        return user_can_update_book


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    context_object_name = "book"
    template_name = "books/book_confirm_delete.html"
    success_url = reverse_lazy("book-list")

    def test_func(self):
        # fn to use w/ https://docs.djangoproject.com/en/5.2/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin
        current_user = self.request.user
        current_object = self.get_object()
        user_can_delete_book = current_object.owner == current_user.profile
        if not user_can_delete_book:
            logger.error(
                f"PermissionDeniedError: {current_user} cannot delete {current_object}."
            )
        return user_can_delete_book
