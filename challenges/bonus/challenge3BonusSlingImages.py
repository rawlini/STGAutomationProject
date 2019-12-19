import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class challenge1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge1(self):
        self.driver.get("https://www.sling.com")
        listCount=len(self.driver.find_elements(By.XPATH, "//*[@id='channelList']/li/img"))
        listCounter=1
        while (listCounter <= listCount):
            print(self.driver.find_element(By.XPATH, "//*[@id='channelList']/li["+str(listCounter)+"]/img").get_attribute('alt'))
            if (listCounter == listCount):
                break
            listCounter += 1

if __name__ == '__main__':
    unittest.main()
