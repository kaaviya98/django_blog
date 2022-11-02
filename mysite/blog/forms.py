from logging import PlaceHolder
from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list(
    "name",
    "name",
)
# choices=[('coding','coding'),('sports','sports'),]
choice_list = []
for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "category", "body")

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "PlaceHolder": "type title"}
            ),
            # "author": forms.Select(
            #   attrs={
            #      "class": "form-control ",
            #      "PlaceHolder": "select author",
            # }
            # ),
            "category": forms.Select(
                choices=choice_list,
                attrs={
                    "class": "form-control",
                    "PlaceHolder": "select author",
                },
            ),
            "body": forms.Textarea(
                attrs={"class": "form-control ", "PlaceHolder": "type ur post"}
            ),
        }
