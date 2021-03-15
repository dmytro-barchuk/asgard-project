from service.models import Comment
from django.forms import ModelForm
from django.core.validators import MinLengthValidator
from django.db import models


class CommentForm(ModelForm):
    
    # name = forms.CharField(max_length=100)
    class Meta:
        model = Comment
        fields = ('name', 'email', 'comment_text')