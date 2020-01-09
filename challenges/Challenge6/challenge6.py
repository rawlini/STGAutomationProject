import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from datetime import datetime

class challenge6(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge6(self):
        self.driver.get("https://www.copart.com")
        searchbar=self.driver.find_element(By.ID,"input-search")
        searchbar.click()
        searchbar.send_keys("nissan skline")
        searchbar.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='serverSideDataTable']/tbody"))
            )
        modelText=self.driver.find_element(By.XPATH,"//*[@id='serverSideDataTable']/tbody/tr[1]/td[6]").text
        firstSearchRow=self.driver.find_element(By.XPATH,"//*[@id='serverSideDataTable']/tbody/tr[1]/td[2]")
        try:
            assertEquals(modelText,"SKYLINE")
        except:
            self.driver.save_screenshot("challenges/Screenshots/challenge6_"+str(datetime.now())+".png")
            raise AssertionError


if __name__ == '__main__':
    unittest.main()