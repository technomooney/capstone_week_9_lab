from selenium.webdriver.firefox.webdriver import WebDriver # i installed firefox webdriver from the apt package manager with 'sudo apt install firefox-geckodriver'
from selenium.webdriver.common.by import By # updated method to find DOM objects. https://www.selenium.dev/documentation/webdriver/elements/finders/

from django.test import LiveServerTestCase

class TitleTest(LiveServerTestCase):
    @classmethod  # setup selenium at the start of the test
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod # tear down the selenium instence after testing is done
    def tearDownClass(cls): 
        cls.selenium.quit()
        super().tearDownClass()


    def test_tile_on_home_page(self):
        self.selenium.get(self.live_server_url)
        self.assertIn('Travel Wishlist',self.selenium.title)


class AddPlacesTest(LiveServerTestCase):
    
    fixtures = ['test_places']

    @classmethod  # setup selenium at the start of the test
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod # tear down the selenium instence after testing is done
    def tearDownClass(cls): 
        cls.selenium.quit()
        super().tearDownClass()

    def test_add_new_place(self):
        
        self.selenium.get(self.live_server_url)

        input_name= self.selenium.find_element(By.ID, 'id_name') # this is the new way to find DOM elements now. https://www.selenium.dev/documentation/webdriver/elements/finders/
        input_name.send_keys('Denver')

        add_button = self.selenium.find_element(By.ID, 'add-new-place')
        add_button.click()

        denver = self.selenium.find_element(By.ID, 'place-name-5')
        self.assertEqual('Denver', denver.text)

        self.assertIn('Denver', self.selenium.page_source) # this still works like it does in the lecture videos 
        self.assertIn('New York', self.selenium.page_source)
        self.assertIn('Tokyo', self.selenium.page_source)


