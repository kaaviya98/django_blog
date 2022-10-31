from logging import PlaceHolder
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "author", "body")

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control ", "PlaceHolder": "type title"}
            ),
            "author": forms.Select(
                attrs={
                    "class": "form-control ",
                    "PlaceHolder": "select author",
                }
            ),
            "body": forms.Textarea(
                attrs={"class": "form-control ", "PlaceHolder": "type ur post"}
            ),
        }
