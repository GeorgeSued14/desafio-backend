import os
from django.test import TestCase

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from dotenv import load_dotenv
load_dotenv()

class RunningAppTest(TestCase):
    
    URL = "http://localhost:8000"
    opt = webdriver.ChromeOptions()


    def setUp(self):
        self.opt.add_argument("--headless")
        self.browser = webdriver.Chrome(
            ChromeDriverManager(log_level=0).install(),
            options=self.opt
        )
        
    def tearDown(self):
        self.browser.quit()

    def test_start_app_django(self):
        self.browser.get(self.URL)
        self.assertIn("Django", self.browser.title)

    def test_settings_path(self):
        setting = os.getenv('DJANGO_SETTINGS_MODULE')
        self.assertIn('core.settings', setting)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
