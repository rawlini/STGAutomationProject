import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge1(self):
        self.driver.get("https://help.sling.com")
        searchbar=self.driver.find_element(By.ID,"support-search-input")
        searchbar.click()
        searchbar.send_keys("TV")
        searchbar.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH,"//*[@class='search-results-list']"))
            )
        searchresult=self.driver.find_element(By.XPATH,"//ul[@class='search-results-list']/section/div/a")
        if searchresult != None:
            x=True    
        self.assertTrue((x,"No Search Results found for TV"))

if __name__ == '__main__':
    unittest.main()