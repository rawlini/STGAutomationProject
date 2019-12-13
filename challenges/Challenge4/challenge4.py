import unittest
from Fibonnaci import *
from IntToString import IntToString as i

class challenge4(unittest.TestCase):

    def test_challenge4(self):
       i.intToString(i,Fibonnaci(60))

if __name__ == '__main__':
    unittest.main()
