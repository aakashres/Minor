from django import forms
from .models import Story, Response, Rating


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = [
            "title",
            "photo",
            "description",
            "content",
            "tag",
            "category",
            "draft",
        ]
        widgets = {
            "title": forms.TextInput(attrs={
                'required': 'True',
                'placeholder': 'Title',
            }),
            "photo": forms.ClearableFileInput(attrs={
                'placeholder': 'Image',
            }
            ),
            "description": forms.Textarea(attrs={
                'required':'true',
                'placeholder': 'Description',
            }
            ),
            "content": forms.Textarea(attrs={
                'required': 'True',
                'placeholder': 'Content',
            }
            ),
            "category": forms.TextInput(attrs={
                'required':'true',
                'placeholder': 'Categories',
            }),
            "draft": forms.CheckboxInput(attrs={
            }),

            "tag": forms.TextInput(attrs={
                'required':'true',
                'placeholder': 'Tags',
            }),



        }



class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = [
            "comment",
        ]

    widgets = {
        "comment": forms.Textarea(attrs={
            'required':'true',
            'placeholder': 'Comment',
        }
        ),
    }
