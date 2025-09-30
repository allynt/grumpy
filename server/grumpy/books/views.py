from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from grumpy.books.models import Book

# from grumpy.books.forms import BookFormSet


@method_decorator(login_required, name="dispatch")
class BookListView(ListView):
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


class BookCreateView(CreateView):
    model = Book
    fields = [
        "title",
        "author",
        "description",
    ]
    template_name = "books/book_form.html"

    def form_valid(self, form):
        current_user = self.request.user
        form.instance.owner = current_user.profile
        return super().form_valid(form)


class BookUpdateView(UpdateView):
    model = Book
    fields = [
        "title",
        "author",
        "description",
    ]
    template_name = "books/book_form.html"


class BookDeleteView(DeleteView):
    model = Book
    context_object_name = "book"
    template_name = "books/book_confirm_delete.html"
    success_url = reverse_lazy("book-list")
