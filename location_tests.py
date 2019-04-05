import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    def test_repr2(self):
        loc = Location("San Fransisco", 40.9, -121.3)
        self.assertEqual(repr(loc),"Location('San Fransisco', 40.9, -121.3)")

    def test_repr3(self):
        loc = Location("New York", 70.1, 99.8)
        self.assertEqual(repr(loc),"Location('New York', 70.1, 99.8)")
    
    def test_eq(self):
        loc = Location("New York", 70.1, 99.8)
        self.assertTrue(loc == Location('New York', 70.1, 99.8))

    def test_eq2(self):
        loc = Location("San Fransisco", 40.9, -121.3)
        self.assertTrue(loc == Location("San Fransisco", 40.9, -121.3))

    def test_eq3(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertTrue(loc == Location("SLO", 35.3, -120.7))


if __name__ == "__main__":
        unittest.main()
