from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(
        required=True, help_text="What do you want?", widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # make sure all the widgets use all the available space
        for field in self.fields.values():
            field.widget.attrs["class"] = "w-100"
