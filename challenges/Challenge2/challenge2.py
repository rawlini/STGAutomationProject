import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from common.Copart.CopartSearchBar import CopartSearchBar

class challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge1(self):
        self.driver.get("https://www.copart.com")
        s=CopartSearchBar(self.driver)
        s.search_input("Exotics")
        searchTable=self.driver.find_element(By.XPATH,"//*[@id='serverSideDataTable']/tbody").text.lower()        
        self.assertIn("porsche",searchTable,"Porsche Not Found in Search Table")

if __name__ == '__main__':
    unittest.main()
