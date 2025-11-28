from django import forms

from grumpy.books.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "description",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # make sure all the widgets make good use of the available space
        for field_name, field_obj in self.fields.items():
            field_obj.widget.attrs["class"] = "w-100"
