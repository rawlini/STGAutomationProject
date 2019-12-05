import unittest
from selenium import webdriver
from Fibonnaci import Fibonnaci as f
from IntToString import IntToString as i

class challenge4(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge4(self):
        i.intToString(i,f.fibonnaciSequence(f,17))

if __name__ == '__main__':
    unittest.main()
