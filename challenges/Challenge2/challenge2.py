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
        self.driver.get("https://www.copart.com")
        searchbar=self.driver.find_element(By.ID,"input-search")
        searchbar.click()
        searchbar.send_keys("exotics")
        searchbar.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='serverSideDataTable']/tbody"))
            )
        searchTable=self.driver.find_element(By.XPATH,"//*[@id='serverSideDataTable']/tbody").text.lower()
        
        self.assertIn("porsche",searchTable,"Porsche Not Found in Search Table")

if __name__ == '__main__':
    unittest.main()
