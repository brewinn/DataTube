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
    search_text = forms.CharField(label='Search text', widget=forms.TextInput(attrs={'placeholder': 'Input search terms...'}))
    search_title = forms.BooleanField(required=False, initial=True)
    search_tags = forms.BooleanField(required=False)
    search_description = forms.BooleanField(required=False)
    full_text_search = forms.BooleanField(required=False)
    sort_by = forms.ChoiceField(
        choices=(
                ('VA', 'Views Ascending'),
                ('VD', 'Views Descending'),
                ('LA', 'Likes Ascending'),
                ('LD', 'Likes Descending'),
                ('DA', 'Dislikes Ascending'),
                ('DD', 'Dislikes Descending'),
                ('CA', 'Comments Ascending'),
                ('CD', 'Comments Descending'),
        )
    )

    @staticmethod
    def modifier_defaults():
        return {
            'search_title': True,
            'search_tags': False,
            'search_description': False,
            'full_text_search': False,
            'sort_by': 'VA',
        }

    def execute_search(self):
        if not self.is_valid():
            raise ValidationError(f"Search form invalid, cannot execute search:{self.errors}")
        data = self.cleaned_data
        search = data.pop('search_text')
        if not any(data.values()):
            return Video.objects.none()

        query = Q()
        if data['full_text_search']:
            if data['search_description']:
                query |= Q(description__search=search)
            if data['search_title']:
                query |= Q(title__search=search)
            if data['search_tags']:
                matches = Tag.objects.filter(tag__search=search)
                matching_videos = {match.videoid for match in matches}
                query |= Q(videoid__in=matching_videos)
        else:
            if data['search_description']:
                query |= Q(description__icontains=search)
            if data['search_title']:
                query |= Q(title__icontains=search)
            if data['search_tags']:
                matches = Tag.objects.filter(tag__icontains=search)
                matching_videos = {match.videoid for match in matches if match.tag == search}
                query |= Q(videoid__in=matching_videos)

        videos = Video.objects.filter(query)

        if data['sort_by'] == 'VA':
            return videos.order_by('views')
        if data['sort_by'] == 'VD':
            return videos.order_by('-views')
        if data['sort_by'] == 'LA':
            return videos.order_by('likes')
        if data['sort_by'] == 'VD':
            return videos.order_by('-likes')
        if data['sort_by'] == 'DA':
            return videos.order_by('dislikes')
        if data['sort_by'] == 'DD':
            return videos.order_by('-dislikes')
        if data['sort_by'] == 'CA':
            return videos.order_by('commentcount')
        if data['sort_by'] == 'CD':
            return videos.order_by('-commentcount')

        return videos

    def find_channel(self, query):
        query = SearchForm.parse_query(query)
        return Channel.objects.filter(channel__exact=query)

    def find_channel_videos(self, query):
        query = SearchForm.parse_query(query)
        return Video.objects.filter(channel__exact=query)

    def find_video(self, query):
        return Video.objects.filter(videoid__exact=query)

    def find_video_tags(self, query):
        found_tags = Tag.objects.filter(videoid__exact=query)
        tags = [tag.tag for tag in found_tags]
        joined_tags = '|'.join(tags)
        return joined_tags


    def find_channel_videos(self, query):
        return Video.objects.filter(channel__exact=query)
        
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

    def r_url(self):
        if not self.is_valid():
            raise ValidationError("Search form invalid, cannot return form url:{self.errors}")
        data = self.cleaned_data
        query = data.pop('search_text')
        url = urlencode({"query": query})
        return url.strip()

    @staticmethod
    def parse_modifiers(modifiers: str) -> dict:
        mod_dict = parse_qs(modifiers)
        parsed_mods = SearchForm.modifier_defaults()
        for key, value in mod_dict.items():
            if key == 'sort_by':
                parsed_mods[key] = value[0]
            else:
                parsed_value = True if value[0] == 'True' else False
                if SearchForm.modifier_defaults()[key] != parsed_value:
                    parsed_mods[key] = parsed_value
        return parsed_mods

    @ staticmethod
    def parse_query(query: str) -> str:
        parsed_query = parse_qs('search_text=' + query)
        decoded_query = parsed_query['search_text'][0]
        return decoded_query

    @ classmethod
    def parse_search(cls, query, modifiers=None):
        query = SearchForm.parse_query(query)
        if not modifiers:
            return cls(data={'search_text': query, **SearchForm.modifier_defaults()})
        parsed_modifiers = SearchForm.parse_modifiers(modifiers)
        return cls(data={'search_text': query, **{**SearchForm.modifier_defaults(), **parsed_modifiers}})
