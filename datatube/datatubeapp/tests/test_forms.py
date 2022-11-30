from .base import initialize_database
from django.test import TestCase
from datatubeapp.forms import SearchForm

# Create your tests here.


class SearchFormTest(TestCase):

    def test_form_search_input_has_placeholder(self):
        form = SearchForm()
        self.assertIn('placeholder="Input search terms..."', form.as_p())

    def test_form_search_yields_results(self):
        initialize_database()
        form = SearchForm(data={'search_text': 'Cat', **SearchForm.modifier_defaults()})
        self.assertEqual(form.execute_search()[0].title, 'Cat video')

    def test_form_url_is_query(self):
        query = 'dog'
        form = SearchForm(data={'search_text': query, **SearchForm.modifier_defaults()})
        expected_form_url = f'query={query}'
        self.assertEqual(form.url(), expected_form_url)

    def test_form_url_contains_modifiers(self):
        query = 'dog'
        modifiers = {'search_title': False, 'search_description': True}
        form = SearchForm(data={'search_text': query, **{**SearchForm.modifier_defaults(), **modifiers}})
        expected_form_url = f'query={query}/modifiers?search_title=False&search_description=True'
        self.assertEqual(form.url(), expected_form_url)

    def test_url_does_not_include_default_modifiers(self):
        query = 'dog'
        modifiers = {'search_title': True, 'search_description': True}
        form = SearchForm(data={'search_text': query, **{**SearchForm.modifier_defaults(), **modifiers}})
        expected_form_url = f'query={query}/modifiers?search_description=True'
        self.assertEqual(form.url(), expected_form_url)

    def test_parse_multiword_search(self):
        encoded_query = 'dog+and+cat'
        parsed_query = SearchForm.parse_query(encoded_query)
        self.assertEqual(parsed_query, 'dog and cat')

    def test_url_encodes_multiword_search(self):
        query = 'dog and cat'
        form = SearchForm(data={'search_text': query, **SearchForm.modifier_defaults()})
        expected_form_url = 'query=dog+and+cat'
        self.assertEqual(form.url(), expected_form_url)
