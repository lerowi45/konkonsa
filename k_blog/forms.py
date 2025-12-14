from django import forms
from .models import KPost

class PostForm(forms.ModelForm):
    class Meta:
        model = KPost
        fields = ["title", "content"]
        