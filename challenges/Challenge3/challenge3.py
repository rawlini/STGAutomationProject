import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge1(self):
        self.driver.get("https://www.copart.com")
        listCount=len(self.driver.find_elements(By.XPATH, "//*[@id='tabTrending']/div[1]/div[2]/div[1]//li"))
        divCount=len(self.driver.find_elements(By.XPATH, "//*[@id='tabTrending']/div[1]/div[2]/div"))
        divCounter=1
        listCounter=1
        while (divCounter != divCount or listCounter <= listCount):
            print(self.driver.find_element(By.XPATH, "//*[@id='tabTrending']/div[1]/div[2]/div["+str(divCounter)+"]//li["+ str(listCounter) +"]/a").text + ' -' + self.driver.find_element(By.XPATH, "//*[@id='tabTrending']/div[1]/div[2]/div["+str(divCounter)+"]//li["+ str(listCounter) +"]/a").get_attribute('href'))
            if (divCounter == divCount and listCounter == listCount):
                break
            if listCounter == listCount:
                divCounter +=1
                listCounter = 1
                continue
            listCounter += 1 

if __name__ == '__main__':
    unittest.main()
