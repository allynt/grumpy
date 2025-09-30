from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from grumpy.meetings.models import Meeting
from grumpy.books.models import Book


@method_decorator(login_required, name="dispatch")
class MeetingListView(ListView):
    model = Meeting
    fields = [
        "book",
        "date",
        "notes",
    ]
    context_object_name = "meetings"
    template_name = "meetings/meeting_list.html"

    def get_queryset(self):
        queryset = Meeting.objects.all()
        return queryset


class MeetingCreateView(CreateView):
    model = Meeting
    fields = [
        "book",
        "date",
        "notes",
    ]
    template_name = "meetings/meeting_form.html"

    def get_initial(self):
        # unread_books = Book.objects.unread()
        unread_books = Book.objects.filter(meeting__isnull=True)
        random_unread_book = unread_books.order_by("?").first()
        return {"book": random_unread_book}
