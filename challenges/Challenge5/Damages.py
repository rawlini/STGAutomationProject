from selenium import webdriver
from selenium.webdriver.common.by import By

class Damages:

    def __init__(self,driver):
        self.driver=driver

    damageCount=[0,0,0,0,0]

    def damage_finder(self,rowCount):
        damageCounter=1
        while(damageCounter<=rowCount):
            damages=self.driver.find_element(By.XPATH,"//*[@id='serverSideDataTable']/tbody/tr["+str(damageCounter)+"]/td[12]/span").text
            damages=str(self.switcher.get(damages))
            self.switch(damages)
            damageCounter+=1        
        print("---DAMAGES---")
        print("REAR END : "+str(self.damageCount[0]))
        print("FRONT END : "+str(self.damageCount[1]))
        print("MINOR DENT/SCRATCHES : "+str(self.damageCount[2]))
        print("UNDERCARRIAGE : "+str(self.damageCount[3]))
        print("MISC : "+str(self.damageCount[4]))

    def RearEnd(self):
        self.damageCount[0]+=1
    def FrontEnd(self):
        self.damageCount[1]+=1
    def DentScratches(self):
        self.damageCount[2]+=1
    def Undercarriage(self):
        self.damageCount[3]+=1
    def Misc(self):
        self.damageCount[4]+=1

    switcher={'REAR END': 'RearEnd','FRONT END': 'FrontEnd', 'MINOR DENT/SCRATCHES':'DentScratches','UNDERCARRIAGE':'Undercarriage'}

    def switch(self,damage):
        return getattr(self,damage,self.Misc)()