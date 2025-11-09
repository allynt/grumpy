from django.contrib import messages
from django.core.mail import mail_managers
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from allauth.account.adapter import get_adapter

from grumpy.books.models import Book
from grumpy.meetings.models import Meeting
from grumpy.core.forms import ContactForm


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Book.objects.all()
        context.update(
            {
                "n_unread_books": books.unread().count(),
                "n_read_books": books.read().count(),
                "meeting": Meeting.objects.future().last(),
            }
        )
        return context


class ContactView(FormView):

    form_class = ContactForm
    template_name = "contact.html"
    success_url = reverse_lazy("help")

    def get_initial(self):
        initial = super().get_initial()
        current_user = self.request.user
        try:
            email = current_user.email
            initial.update({"email": current_user.email})
        except AttributeError as e:
            pass
        return initial

    def form_valid(self, form):

        try:
            adapter = get_adapter(self.request)
            mail_managers(
                adapter.format_email_subject("Contact Form"),
                render_to_string("email/contact.txt", form.cleaned_data),
                fail_silently=False,
            )
            msg = "Your message has been sent.  Bear with me, I'll read it eventually."
            messages.add_message(self.request, messages.SUCCESS, msg)
        except Exception as e:
            msg = "Something went wrong.  Your message has not been sent."
            messages.add_message(self.request, messages.ERROR, msg)

        return super().form_valid(form)


class HelpView(TemplateView):
    template_name = "help.html"
