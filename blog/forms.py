from django import forms

class EntryForm(forms.Form):
    commenter = forms.CharField(label='Name', max_length=100, required=False)
    comment = forms.CharField(label='Comment', widget=forms.Textarea, required=False)
