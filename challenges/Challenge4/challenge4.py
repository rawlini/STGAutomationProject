import unittest
from Fibonnaci import *
from IntToString import IntToString as i
from DriverInit import DriverInit as d

d.init(d)
d.tearDown(d)

class challenge4(unittest.TestCase):

    def test_challenge4(self):
       i.intToString(i,Fibonnaci(50))

if __name__ == '__main__':
    unittest.main()
