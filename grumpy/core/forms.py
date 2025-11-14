from django import forms

from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(
        required=True, help_text="What do you want?", widget=forms.Textarea
    )
    captcha = CaptchaField(label="Enter the text in the image")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # make sure all the widgets make good use of the available space
        for field_name, field_obj in self.fields.items():
            if field_name == "captcha":
                field_obj.widget.attrs["class"] = "w-25"
            else:
                field_obj.widget.attrs["class"] = "w-100"
