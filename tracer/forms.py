from django import forms
from taggit.forms import *
from tracer.models import Dream
from datetime import datetime
from django.forms.extras.widgets import SelectDateWidget

class DreamForm(forms.Form):
    title = forms.CharField(label="Title", max_length=50)
    description = forms.CharField(label="Description", max_length=4000, widget=forms.Textarea(attrs={'rows':6}))
    rating = forms.CharField( max_length=1, widget=forms.Select(choices=Dream.RATING_CHOICES, attrs={'class':'ui dropdown'}), initial='3')
    location = forms.CharField(label="Location", max_length=50)
    theme = TagField()
    date = forms.DateField(widget=SelectDateWidget(attrs={'class':'ui dropdown'}), initial=datetime.now)
