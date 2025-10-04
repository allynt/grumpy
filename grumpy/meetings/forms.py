from django import forms
from grumpy.meetings.models import Meeting


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = [
            "book",
            "date",
            "notes",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # make sure users can't modify an assigned boook
        # (or use the widget to see other available books)
        self.fields["book"].disabled = True
