from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from grumpy.meetings.forms import MeetingForm
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


class MeetingCreateView(UserPassesTestMixin, CreateView):
    model = Meeting
    form_class = MeetingForm  # custom form ensures "book" is read-only
    template_name = "meetings/meeting_form.html"
    success_url = reverse_lazy("meeting-list")

    def test_func(self):
        # restrict view to admins only,
        # as per https://docs.djangoproject.com/en/5.2/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin
        # TODO: EVEN THOUGH THIS IS THE RECOMMENDED METHOD, IT'S A BIT OBFUSCATED; REPLACE W/ DECORATOR
        return self.request.user.is_superuser

    def get_initial(self):
        # unread_books = Book.objects.unread()
        unread_books = Book.objects.filter(meeting__isnull=True)
        random_unread_book = unread_books.order_by("?").first()
        return {"book": random_unread_book}
