from django.forms import ModelForm, TextInput, Textarea

from my_book_shop.models import Book


class AddBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ("title", "text")
        widgets = {
            'title': TextInput(attrs={'class': "form-control"}),
            "text": Textarea(attrs={'class': "form-control"})
        }