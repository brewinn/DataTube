from .base import initialize_database
from datatubeapp.forms import SearchForm
from django.test import TestCase
from unittest import skip

# Create your tests here.
class HomePageTest(TestCase):


    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        
    def test_home_page_uses_search_form(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], SearchForm)

class SearchViewTest(TestCase):

    def test_can_search_using_a_POST_request(self):
        initialize_database()
        response = self.client.post('/', data={'search_text':'cat'}, follow=True)
        self.assertIn('cat', response.content.decode().lower())
        self.assertTemplateUsed(response, 'search.html')

    def test_search_result_appears_in_table(self):
        initialize_database()
        response = self.client.post('/', data={'search_text':'dog'}, follow=True)
        self.assertIn('dog video', response.content.decode())
        self.assertTemplateUsed(response, 'search.html')

    def test_unrelated_items_do_not_appear_in_table(self):
        initialize_database()
        response = self.client.post('/', data={'search_text':'dog'}, follow=True)
        self.assertNotIn('Cat', response.content.decode())
        self.assertTemplateUsed(response, 'search.html')
        
        
    def test_search_POST_redirects_to_SearchView(self):
        data={'search_text':'search text'}
        response = self.client.post('/', data=data)
        self.assertEqual(response.status_code, 302)
        expected_url = '/search/' + SearchForm(data=data).url()
        self.assertEqual(response['location'], expected_url)

