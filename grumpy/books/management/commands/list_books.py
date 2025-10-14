import json

from django.core.management.base import BaseCommand, CommandError
from django.db.models import Count, Q
from django.utils.translation import gettext_lazy as _

from grumpy.users.models import UserProfile


class Command(BaseCommand):
    """
    Outputs the number of books owned by users according to their statuses.
    """

    help = "Outputs the number of books owned by users according to their statuses."

    def add_arguments(self, parser):
      
        parser.add_argument(
            "--read", action="store_true", help=_("Only list read books.")
        )
        parser.add_argument(
            "--unread", action="store_true", help=_("Only list unread books.")
        )
        parser.add_argument("--all", action="store_true", help=_("List all books."))

    def handle(self, *args, **options):

        n_options = [
            v for k, v in options.items() if k in ["read", "unread", "all"]
        ].count(True)
        if n_options != 1:
            raise CommandError("One of '--read' or '--unread' or '--all' is required.")

        try:

            if options["read"]:
                filter_kwargs = {"books__meeting__isnull": False}
            elif options["unread"]:
                filter_kwargs = {"books__meeting__isnull": True}
            else:  # options["all"]:
                filter_kwargs = {}

            qs = (
                # not the most efficient query but whatever...
                UserProfile.objects.values_list("user__email")
                .annotate(n_books=Count("books", filter=Q(**filter_kwargs)))
                .order_by("user__email")
            )
            pretty_qs = json.dumps(dict(qs), indent=4)
            self.stdout.write(self.style.SUCCESS(pretty_qs))

        except Exception as e:
            raise CommandError(str(e))
