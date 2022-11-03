from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time
import os

from datatubeapp.tests.base import initialize_database

MAX_WAIT = 1

class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        command_executor = os.environ.get("WEBDRIVER_EXECUTOR")
        if command_executor:
            self.browser = webdriver.Remote(
                command_executor=command_executor,
                options=webdriver.FirefoxOptions()
                )
        else:
            options=webdriver.FirefoxOptions()
            options.add_argument('--headless')
            self.browser = webdriver.Firefox(options=options)
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server
        initialize_database()

    def tearDown(self):
        self.browser.quit()

    def wait_for_active_query(self):
        start_time = time.time()
        while True:
            try:
                self.browser.find_element(By.ID, 'active_query')
                return
            except (WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
    
    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, 'id_search_results')
                cells = table.find_elements(By.TAG_NAME, 'td')
                self.assertTrue(any([row_text in cell.text for cell in cells]), f"Couldn't find {row_text} in {[cell.text for cell in cells]}")
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def get_search_box(self):
        return self.browser.find_element(By.ID, 'id_search_text')
