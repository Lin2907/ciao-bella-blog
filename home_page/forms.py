from .models import Comment
from django import forms
from .models import Tag


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

# Form for adding Tags
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']