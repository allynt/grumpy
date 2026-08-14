import copy
import logging

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import mail_managers
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from allauth.account.adapter import get_adapter

from grumpy.core.utils import is_error
from grumpy.books.forms import BookForm
from grumpy.books.models import Book

logger = logging.getLogger(__name__)


def notify(request, subject, message):
    adapter = get_adapter(request)
    subject = adapter.format_email_subject(subject)
    message = f"{message} [{get_current_site(request)}]"
    mail_managers(subject, message, fail_silently=True)


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
    form_class = BookForm
    template_name = "books/book_form.html"
    success_url = reverse_lazy("book-list")

    def form_valid(self, form):
        current_user = self.request.user
        form.instance.owner = current_user.profile
        response = super().form_valid(form)
        if not is_error(response.status_code):
            messages.add_message(
                self.request, messages.SUCCESS, f'Successfully added "{self.object}".'
            )

            if settings.NOTIFY_BOOKS:
                notify(
                    self.request,
                    "new book created",
                    f"User {current_user} created a new book: {self.object.id}.",
                )

        return response

    def test_func(self):
        # fn to use w/ https://docs.djangoproject.com/en/5.2/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin
        current_user = self.request.user
        user_can_add_books = current_user.profile.can_add_books
        if not user_can_add_books:
            logger.error(f"PermissionDeniedError: {current_user} cannot add books.")
        return user_can_add_books


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    form_class = BookForm
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

    def form_valid(self, form):
        response = super().form_valid(form)
        if not is_error(response.status_code):
            messages.add_message(
                self.request, messages.SUCCESS, f'Successfully updated "{self.object}".'
            )
        return response


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

    def form_valid(self, form):
        deleted_book = copy.copy(
            self.object
        )  # shallow copy to refer to book details after it's been deleted
        response = super().form_valid(form)
        if not is_error(response.status_code):
            messages.add_message(
                self.request, messages.SUCCESS, f'Successfully deleted "{self.object}".'
            )

            if settings.NOTIFY_BOOKS:
                notify(
                    self.request,
                    "book deleted",
                    f"User {self.request.user} deleted a book: {deleted_book.id}.",
                )

        return response
