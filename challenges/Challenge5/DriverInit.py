from selenium import webdriver

class DriverInit:
    
    def init(self):
        self.driver = webdriver.Chrome("chromedriver")

    def tearDown(self):
        self.driver.close()