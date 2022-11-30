from .base import initialize_database
from datatubeapp.forms import SearchForm
from django.test import TestCase
from django.utils.html import escape

# Create your tests here.


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'base.html')

    def test_home_page_uses_search_form(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], SearchForm)


class SearchViewTest(TestCase):

    def test_can_search_using_a_POST_request(self):
        initialize_database()
        response = self.client.post('/', data={'search_text': 'cat', **SearchForm.modifier_defaults()}, follow=True)
        self.assertIn('cat', response.content.decode().lower())
        self.assertTemplateUsed(response, 'base.html')

    def test_search_query_appears_in_response(self):
        initialize_database()
        response = self.client.post('/', data={'search_text': 'dog', **SearchForm.modifier_defaults()}, follow=True)
        self.assertIn('Active Query: dog', response.content.decode())

    def test_search_modifiers_appears_in_response(self):
        initialize_database()
        response = self.client.post('/', data={**SearchForm.modifier_defaults(), 'search_text': 'dog', 'search_title': False, 'search_description': True}, follow=True)
        self.assertIn(escape("'search_title': False"), response.content.decode())
        self.assertIn(escape("'search_description': True"), response.content.decode())

    def test_search_result_appears_in_table(self):
        initialize_database()
        response = self.client.post('/', data={'search_text': 'dog', **SearchForm.modifier_defaults()}, follow=True)
        self.assertIn('dog video', response.content.decode())

    def test_unrelated_items_do_not_appear_in_table(self):
        initialize_database()
        response = self.client.post('/', data={'search_text': 'dog', **SearchForm.modifier_defaults()}, follow=True)
        self.assertNotIn('Cat', response.content.decode())

    def test_search_with_no_results_gives_informative_response(self):
        initialize_database()
        response = self.client.post('/', data={'search_text': 'mango', **SearchForm.modifier_defaults()}, follow=True)
        self.assertIn('No videos found', response.content.decode())

    def test_search_POST_redirects_to_SearchView(self):
        data = {'search_text': 'search text', **SearchForm.modifier_defaults()}
        response = self.client.post('/', data=data)
        self.assertEqual(response.status_code, 302)
        expected_url = '/search/' + SearchForm(data=data).url()
        self.assertEqual(response['location'], expected_url)
