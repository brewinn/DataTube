from .base import initialize_database
from django.test import TestCase
from datatubeapp.forms import SearchForm
from datatubeapp.models import Video

# Create your tests here.
class SearchFormTest(TestCase):

    def test_form_search_input_has_placeholder(self):
        form = SearchForm()
        self.assertIn('placeholder="Input search terms..."', form.as_p())

    def test_form_validation_for_long_searches(self):
        hundred_letter_search = SearchForm(
                data={
                    'search_text':'0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789',
                    **SearchForm.modifier_defaults(),
                    }
                )
        self.assertTrue(hundred_letter_search.is_valid(), f"Failed to validate search: {hundred_letter_search.errors}")
        
        hundred_plus_one_letter_search = SearchForm(
                data={
                    'search_text':'01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890',
                    **SearchForm.modifier_defaults(),
                    }
                )
    
        self.assertFalse(hundred_plus_one_letter_search.is_valid(), f"Search is valid, but shouldn't be")

    def test_form_search_yields_results(self):
        initialize_database()
        form = SearchForm(data={'search_text':'Cat', **SearchForm.modifier_defaults()})
        self.assertEqual(form.execute_search()[0].title , 'Cat video')

    def test_form_url_is_query(self):
        query = 'dog'
        form = SearchForm(data={'search_text':query, **SearchForm.modifier_defaults()})
        expected_form_url = f'query={query}'
        self.assertEqual(form.url(), expected_form_url)
    
    def test_form_url_contains_modifiers(self):
        query = 'dog'
        modifiers = {'search_title':False,'search_description':True}
        form = SearchForm(data={'search_text':query, **modifiers})
        expected_form_url = f'query={query}/modifiers?search_title=False&search_description=True'
        self.assertEqual(form.url(), expected_form_url)

    def test_url_does_not_include_default_modifiers(self):
        query = 'dog'
        modifiers = {'search_title':True,'search_description':True}
        form = SearchForm(data={'search_text':query, **modifiers})
        expected_form_url = f'query={query}/modifiers?search_description=True'
        self.assertEqual(form.url(), expected_form_url)
        
    def test_parse_modifiers_returns_dictionary(self):
        modifiers='search_title=False&search_description=True'
        parsed_modifiers = SearchForm.parse_modifiers(modifiers)
        self.assertEqual(parsed_modifiers, {'search_title':False, 'search_description':True})
