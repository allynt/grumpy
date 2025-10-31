from django import forms
from django.contrib.gis import forms as gis_forms

from bootstrap_datepicker_plus.widgets import DateTimePickerInput

from grumpy.books.models import Book
from grumpy.meetings.models import Meeting, DEFAULT_LOCATION


FORM_DATETIME_FORMAT_CODE = "YYYY-MM-DD HH:MM"


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = [
            "book",
            "date",
            "status",
            "notes",
            "location",
        ]
        widgets = {
            # using 3rd party DatePicker support b/c
            # I can't be bothered to write my own
            "date": DateTimePickerInput(
                options={
                    "format": FORM_DATETIME_FORMAT_CODE,
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

    location = gis_forms.PointField(
        widget=gis_forms.OSMWidget(
            attrs={
                "map_width": 400,  # not working; set in "base.css" instead
                "map_height": 400,  # not working; set in "base.css" instead
                "default_zoom": DEFAULT_LOCATION.zoom,
                "default_lat": DEFAULT_LOCATION.latitude,
                "default_lon": DEFAULT_LOCATION.longitude,
            }
        )
    )
