from selenium import webdriver

class DriverInit:

    def __init__(self,driver):
        self.driver=driver
    
    def init(self):
        self.driver = webdriver.Chrome("chromedriver")

    def tearDown(self):
        self.driver.close()