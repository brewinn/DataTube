from .base import FunctionalTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class SearchValidationTest(FunctionalTest):

    def test_cannot_break_search_with_special_characters(self):
        # A mischievous monkey finds its way onto the site.
        self.browser.get(self.live_server_url)

        # Noticing the search box, he tries throwing some strange characters in
        # to see if it breaks. 
        inputbox = self.get_search_box()
        inputbox.send_keys('#print(":^)")')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_active_query()

        ## If something breaks, the search box will fail to appear.
        inputbox = self.get_search_box()
        inputbox.send_keys('"')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_active_query()
        
        inputbox = self.get_search_box()
        inputbox.send_keys("\\")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_active_query()

        inputbox = self.get_search_box()
        inputbox.send_keys('--')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_active_query()
        
        inputbox = self.get_search_box()
        inputbox.send_keys("'")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_active_query()
        
        # Nothing seems to work, so he leaves for the time being.

    def test_cannot_make_an_empty_search(self):
        # Another monkey was let lose on the site
        self.browser.get(self.live_server_url)

        # This one wonders about the void... what does an empty search do?
        home_url = self.browser.current_url
        inputbox = self.get_search_box()
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_active_query()

        # A popup appears, but no search starts.
        self.assertEqual(self.browser.current_url, home_url)

        # Undeterred, the monkey puts in a normal search.
        inputbox = self.get_search_box()
        inputbox.send_keys(':^]')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_active_query()
        search_url = self.browser.current_url

        # Seeing that the normal search succeeded, he tries the empty search again.
        inputbox = self.get_search_box()
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_active_query()

        # Again, no luck
        self.assertEqual(self.browser.current_url, search_url)
        
