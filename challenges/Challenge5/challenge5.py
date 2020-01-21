import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Damages import Damages
from Models import Models
from common.Copart.CopartSearchBar import CopartSearchBar

class challenge5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge5(self):
        self.driver.get("https://www.copart.com")
        s=CopartSearchBar(self.driver)
        model="porsche"
        s.search_input(model)
        entryNumber100=self.driver.find_element(By.XPATH,"//*[@id='serverSideDataTable_length']//option[3]")
        entryNumber100.click()
        WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='serverSideDataTable']/tbody/tr[100]"))
            )
        m=Models(self.driver)
        m.unique_model_counter(100)
        d=Damages(self.driver)
        d.damage_finder(100)
                
                


if __name__ == '__main__':
    unittest.main()
