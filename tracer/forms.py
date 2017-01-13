from django import forms
from taggit.forms import *
from tracer.models import Dream

class DreamForm(forms.Form):
    title = forms.CharField(label="Title", max_length=50)
    description = forms.CharField(label="Description", max_length=4000, widget=forms.Textarea)
    rating = forms.CharField( max_length=1, widget=forms.Select(choices=Dream.RATING_CHOICES), initial='3')
    location = forms.CharField(label="Location", max_length=50)
    theme = TagField()
