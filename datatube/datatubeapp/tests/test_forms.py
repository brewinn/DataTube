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
                    'search_text':'0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
                    }
                )
        self.assertTrue(hundred_letter_search.is_valid(), f"Failed to validate search: {hundred_letter_search.errors}")
        
        hundred_plus_one_letter_search = SearchForm(
                data={
                    'search_text':'01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890'
                    }
                )
    
        self.assertFalse(hundred_plus_one_letter_search.is_valid(), f"Search is valid, but shouldn't be")

    def test_form_search_yields_results(self):
        initialize_database()
        form = SearchForm(data={'search_text':'Cat'})
        self.assertEqual(form.execute_search()[0].title , 'Cat video')

    def test_form_url_is_query_plus_modifiers(self):
        query = 'dog'
        form = SearchForm(data={'search_text':query})
        expected_form_url = f'query={query}'
        self.assertEqual(form.url(), expected_form_url)
