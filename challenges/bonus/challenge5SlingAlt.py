import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class challenge1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge1(self):
        self.driver.get("https://www.sling.com")
        pagetags = self.driver.find_elements(By.XPATH,"//*")
        WebDriverWait(self.driver,60).until(
            expected_conditions.presence_of_all_elements_located((By.XPATH,"//*[@id='hp_deviceoffers']"))
        )
        altTagCount=0
        for e in pagetags:
            if e.get_attribute("alt") != None:
                print(e.get_attribute("alt"))
                altTagCount +=1
        print ("There are "+str(altTagCount)+" Alt Tags on this HTML page")

            


if __name__ == '__main__':
    unittest.main()
