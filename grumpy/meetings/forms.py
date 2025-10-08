from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django import forms
from grumpy.meetings.models import Meeting

DATETIME_FORMAT_CODE = "YYYY-MM-DD HH:MM"


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = [
            "book",
            "date",
            "notes",
        ]
        widgets = {
            # using 3rd party DatePicker support
            # b/c I can't be bothered to write my own
            "date": DateTimePickerInput(
                options={
                    "format": DATETIME_FORMAT_CODE,
                    "showTodayButton": False,
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # make sure users can't modify an assigned book
        # (nor use the widget to see other books)
        self.fields["book"].disabled = True
