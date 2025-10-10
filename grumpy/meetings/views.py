import logging

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from grumpy.meetings.forms import MeetingForm
from grumpy.meetings.models import Meeting
from grumpy.books.models import Book

logger = logging.getLogger(__name__)


class MeetingListView(LoginRequiredMixin, ListView):
    model = Meeting
    fields = [
        "book",
        "date",
        "notes",
    ]
    context_object_name = "meetings"
    template_name = "meetings/meeting_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["n_unread_books"] = Book.objects.unread().count()
        return context

    def get_queryset(self):
        queryset = Meeting.objects.all()
        return queryset


class MeetingCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Meeting
    form_class = MeetingForm  # custom form ensures "book" is non-editable
    template_name = "meetings/meeting_form.html"
    success_url = reverse_lazy("meeting-list")

    def test_func(self):
        # fn to use w/ https://docs.djangoproject.com/en/5.2/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin
        current_user = self.request.user
        user_is_special = current_user.profile.is_special
        if not user_is_special:
            logger.error(f"PermissionDeniedError: {current_user} cannot add meetings.")
        return user_is_special

    def get_initial(self):
        random_unread_book = Book.objects.unread().random()
        return {"book": random_unread_book}
