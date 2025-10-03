from django.views.generic import TemplateView

from grumpy.books.models import Book


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Book.objects.all()
        context.update(
            {
                "n_unread_books": books.filter(meeting__isnull=True).count(),
                "n_read_books": books.filter(meeting__isnull=False).count(),
            }
        )
        return context


class HelpView(TemplateView):
    template_name = "help.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
