from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_search_and_revisit_it_later(self):
        # A user (say, John) wants to visit our site. He navigates to our homepage.
        self.browser.get('http://localhost:8000')

        # He notices the page title and header
        self.assertIn('DataTube', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('DataTube', header_text)

        # He's invited to do a search
        inputbox = self.browser.find_element(By.ID, 'id_search_text')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Search...'
                )

        # He inputs 'cat' into the text box
        inputbox.send_keys('cat')

        # He hits enter, the page updates, and now the page lists some search results
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, 'id_search_results')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertTrue(
                any('cat' in row.text for row in rows)
                )

        # The search box persists, inviting another search. John decides to search 'dog'
        # this time.
        self.fail("Finish the test!")

        # The page updates again, and new results are shown.

        # John likes the results, and wants to save them for later. He notices
        # that the url has changed to reflect their search.

        # John visits that url directly -- the search is the same.

        # Satisfied, he heads off to sleep.

if __name__ == "__main__":
    unittest.main(warnings='ignore')
