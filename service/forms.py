from service.models import Comment
from django import forms
from django.forms import ModelForm

class CommentForm(ModelForm):
    # name = forms.CharField(max_length=100)
    class Meta:
        model = Comment
        fields = ('name', 'email', 'comment_text')