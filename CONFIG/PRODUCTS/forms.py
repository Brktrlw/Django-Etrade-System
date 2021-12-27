from django import forms
from .models import ProductCommentsModel


class CommentForm(forms.ModelForm):
    class Meta:
        model=ProductCommentsModel
        fields=["commentText"]