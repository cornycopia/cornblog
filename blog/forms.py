from django import forms
from django.forms import ModelForm
from .models import Comment

class EntryForm(forms.Form):
    commenter = forms.CharField(label='Name', max_length=100, required=False)
    comment = forms.CharField(label='Comment', widget=forms.Textarea, required=False)

class CommentForm(ModelForm):
    model = Comment
    fields = ['entry', 'pub_date', 'commenter', 'comment_text', 'score']
