import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from datetime import datetime
from common.Copart.CopartSearchBar import CopartSearchBar
from common.Copart.CopartSearchFilter import CopartSearchFilter
from common.Screenshot import Screenshot

class challenge6(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge6(self):
        try:
            self.driver.get("https://www.copart.com")
            s=CopartSearchBar(self.driver)
            make="Nissan"
            model="Skyline"
            s.search_input(make)
            f=CopartSearchFilter(self.driver)
            f.modelFilter.click()
            f.firstModelText.text.upper()
            self.assertEqual(firstModelText,model.upper())
        except:
            sc=Screenshot(self.driver)
            sc.screencapture(challenge6)
            raise AssertionError


if __name__ == '__main__':
    unittest.main()