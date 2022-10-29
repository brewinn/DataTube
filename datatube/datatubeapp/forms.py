"""
Forms are Django's way of dealing with user input. While we could just
manually process post data, it's more robust to use the validation that forms
provide.
"""

from django import forms
from django.utils.html import urlencode
from django.core.exceptions import ValidationError
from datatubeapp.models import Video

class SearchForm(forms.Form):
    '''This is the form for searching for videos/channels.'''
    search_text = forms.CharField(label='Search text', max_length=100, widget=forms.TextInput(attrs={'placeholder':'Input search terms...'}))

    def execute_search(self):
        if not self.is_valid():
                raise ValidationError("Search form invalid, cannot execute search:{self.errors}")
        return Video.objects.filter(title__contains=self.cleaned_data['search_text'])

    def url(self):
        if not self.is_valid():
                raise ValidationError("Search form invalid, cannot return form url:{self.errors}")
        data = self.cleaned_data
        return urlencode({"query":f"{data['search_text']}"})


    @classmethod
    def parse_query(cls,query):
            
            return SearchForm(data={'search_text':query})
        
