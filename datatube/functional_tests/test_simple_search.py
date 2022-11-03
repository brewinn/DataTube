from .base import FunctionalTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

class NewVisitorTest(FunctionalTest):
    
    def test_can_start_a_search_and_revisit_it_later(self):
        # A user (say, John) wants to visit our site. He navigates to our homepage.
        self.browser.get(self.live_server_url)

        # He notices the page title and header
        self.assertIn('DataTube', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('DataTube', header_text)

        # He's invited to do a search
        inputbox = self.get_search_box()
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Input search terms...'
                )

        # He inputs 'cat' into the text box
        inputbox.send_keys('cat')

        # He hits enter, the page updates, and now the page lists some search results
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('Cat')

        # The search box persists, inviting another search. John decides to search 'dog'
        # this time.
        inputbox = self.get_search_box()
        inputbox.send_keys('dog')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and new results are shown.
        self.wait_for_row_in_list_table('dog')

        # John likes the results, and wants to save them for later. He notices
        # that the url has changed to reflect their search.
        search_url = self.browser.current_url
        self.assertRegex(search_url, '/query=.+')

        # John visits that url directly -- the search is the same.
        self.browser.get(search_url)
        self.wait_for_row_in_list_table('dog')

        # Satisfied, he heads off to sleep.

    def test_can_search_with_a_modifier(self):

        # John wants to make a new search.
        self.browser.get(self.live_server_url)

        # He's looking for a more specific result. He wants to find videos that
        # mention dogs in the description, but not the title.
        title_checkbox = self.browser.find_element(By.ID, 'id_search_title')
        title_checkbox.click()
        
        description_checkbox = self.browser.find_element(By.ID, 'id_search_description')
        description_checkbox.click()
        
        inputbox = self.get_search_box()
        inputbox.send_keys('dog')
        inputbox.send_keys(Keys.ENTER)

        # He checks the results ... good.
        self.wait_for_row_in_list_table('Cat video')
        page_body = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('dog video', page_body)
        
        # He checks the url and sees and new `modifiers` section 
        url = self.browser.current_url
