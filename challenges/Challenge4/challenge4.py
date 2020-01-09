import unittest
from Fibonnaci import *
from IntToString import IntToString as i
from random import randint
from random import seed

class challenge4(unittest.TestCase):

    def test_challenge4(self):
        value=randint(0,93)
        print("The "+str(value)+" number in fibonacci is "+str(i.intToString(i,Fibonnaci(value)))+".")

if __name__ == '__main__':
    unittest.main()
