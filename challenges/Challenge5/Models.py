from selenium import webdriver
from selenium.webdriver.common.by import By

class Models:
    def __init__(self,driver):
        self.driver=driver

    def model_finder(self,rowCount):
        modelArray=[]
        rowCounter=1
        while (rowCounter<=rowCount):
            model=self.driver.find_element(By.XPATH,"//*[@id='serverSideDataTable']/tbody/tr["+str(rowCounter)+"]/td[6]/span").text
            modelArray.append(model)
            rowCounter+=1
        uniqueModels=set(modelArray)
        uniqueModelsLength=len(uniqueModels)
        return uniqueModels,modelArray,uniqueModelsLength

    def unique_model_counter(self,rowCount):
        uniqueModels, modelArray, uniqueModelsLength=self.model_finder(rowCount)
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