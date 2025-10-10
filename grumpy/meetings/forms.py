from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django import forms

from grumpy.books.models import Book
from grumpy.meetings.models import Meeting

DATETIME_FORMAT_CODE = "YYYY-MM-DD HH:MM"


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = [
            "book",
            "date",
            "status",
            "notes",
        ]
        widgets = {
            # using 3rd party DatePicker support b/c
            # I can't be bothered to write my own
            "date": DateTimePickerInput(
                options={
                    "format": DATETIME_FORMAT_CODE,
                    "showTodayButton": False,
                }
            ),
        }

    book = forms.ModelChoiceField(
        # a bit of HACKERY to ensure that the initial book cannot be changed; if I
        # don't specify "to_field_name", then Django just uses "pk", and by specifying
        # readonly" instead of "disabled" I ensure Django still POSTS the data, and
        # using "TextInput" widget limits the value to a single choice (and the standard
        # "Select" wdidget cannot be "readonly").
        queryset=Book.objects.unread(),
        required=True,
        to_field_name="title",
        widget=forms.TextInput(attrs={"readonly": "readonly"}),
    )
