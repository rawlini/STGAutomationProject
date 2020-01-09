import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Damages import Damages

class challenge5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge5(self):
        self.driver.get("https://www.copart.com")
        searchbar=self.driver.find_element(By.ID,"input-search")
        searchbar.click()
        searchbar.send_keys("porsche")
        searchbar.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='serverSideDataTable']/tbody"))
            )
        entryNumber100=self.driver.find_element(By.XPATH,"//*[@id='serverSideDataTable_length']//option[3]")
        entryNumber100.click()
        WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='serverSideDataTable']/tbody/tr[100]"))
            )
        rowCounter=1
        modelArray=[]
        while (rowCounter<=100):
            model=self.driver.find_element(By.XPATH,"//*[@id='serverSideDataTable']/tbody/tr["+str(rowCounter)+"]/td[6]/span").text
            modelArray.append(model)
            rowCounter+=1
        uniqueModels=set(modelArray)
        uniqueModelsLength=len(uniqueModels)
        modelCounter=0
        modelnum=0
        i=1
        print("---MODELS---")
        while(uniqueModelsLength>modelCounter):
            if(list(uniqueModels)[modelCounter]==modelArray[i]):
                modelnum+=1
                i+=1
            else:
                i+=1                               
            if(i==100):
                print(str(list(uniqueModels)[modelCounter]) + " : " + str(modelnum))
                i=1
                modelCounter+=1
                modelnum=0
        d=Damages(self.driver)
        d.damage_finder(100)
                
                


if __name__ == '__main__':
    unittest.main()
