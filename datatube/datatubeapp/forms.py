"""
Forms are Django's way of dealing with user input. While we could just
manually process post data, it's more robust to use the validation that forms
provide.
"""

from django import forms
from django.utils.html import urlencode
from django.core.exceptions import ValidationError
from django.db.models import Q
from datatubeapp.models import Video, Channel, Tag
from urllib.parse import parse_qs


class SearchForm(forms.Form):
    '''This is the form for searching for videos/channels.'''
    search_text = forms.CharField(label='Search text', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Input search terms...'}))
    search_title = forms.BooleanField(required=False, initial=True)
    search_description = forms.BooleanField(required=False)

    @staticmethod
    def modifier_defaults():
        return {
            'search_title': True,
            'search_description': False,
        }

    def execute_search(self):
        if not self.is_valid():
            raise ValidationError("Search form invalid, cannot execute search:{self.errors}")
        data = self.cleaned_data
        if not data['search_title'] and not data['search_description']:
            return Video.objects.none()

        query = Q()
        if data['search_description']:
            query |= Q(description__icontains=data['search_text'])
        if data['search_title']:
            query |= Q(title__icontains=data['search_text'])

        return Video.objects.filter(query)

    def find_channel(self, query):
        return Channel.objects.filter(channel__exact=query)

    def find_channel_videos(self, query):
        return Video.objects.filter(channel__exact=query)

    def find_video(self, query):
        return Video.objects.filter(videoid__exact=query)

    def find_video_tags(self, query):
        found_tags = Tag.objects.filter(videoid__exact=query)
        tags = [tag.tag for tag in found_tags]
        joined_tags = '|'.join(tags)
        return joined_tags

    def url(self):
        if not self.is_valid():
            raise ValidationError("Search form invalid, cannot return form url:{self.errors}")
        data = self.cleaned_data

        query = data.pop('search_text')
        modifiers = data

        # If all modifiers are the default, just use the query
        if modifiers == SearchForm.modifier_defaults():
            return urlencode({"query": query})

        # Only encode modifiers that are not the default
        url_mods = {key: value for key, value in modifiers.items() if modifiers[key] != SearchForm.modifier_defaults()[key]}
        url = urlencode({"query": query}) + '/modifiers?' + urlencode({**url_mods})
        return url.strip()

    @staticmethod
    def parse_modifiers(modifiers: str) -> dict:
        mod_dict = parse_qs(modifiers)
        parsed_mods = {}
        for key, value in mod_dict.items():
            parsed_value = True if value[0] == 'True' else False
            if SearchForm.modifier_defaults()[key] != parsed_value:
                parsed_mods[key] = parsed_value
        return parsed_mods

    @staticmethod
    def parse_query(query: str) -> str:
        parsed_query = parse_qs('search_text=' + query)
        decoded_query = parsed_query['search_text'][0]
        return decoded_query

    @classmethod
    def parse_search(cls, query, modifiers=None):
        query = SearchForm.parse_query(query)
        if not modifiers:
            return cls(data={'search_text': query, **SearchForm.modifier_defaults()})
        parsed_modifiers = SearchForm.parse_modifiers(modifiers)
        return cls(data={'search_text': query, **parsed_modifiers})
