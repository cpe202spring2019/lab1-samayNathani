import unittest
from lab1 import *

class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        tlist = None
        with self.assertRaises(ValueError):
            max_list_iter(tlist)
    
    def test_max_list_iter2(self):
        l = [7,6,5,4]
        self.assertEqual(max_list_iter(l), 7)
    
    def test_max_list_iter3(self):
        l = [2,2.001,1,2,0]
        self.assertEqual(max_list_iter(l), 2.001)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
    
    def test_reverse_rec2(self):
        l = None
        with self.assertRaises(ValueError):
            reverse_rec(l)
    
    def test_reverse_rec3(self):
        self.assertEqual(reverse_rec([1,1,0]),[0,1,1])

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

    def test_bin_search2(self):
        list_val =[0,1,2,3]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0)

    def test_bin_search3(self):
        list_val =[0,1,2,3,4,5,6,7,8,9]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(9, 0, len(list_val)-1, list_val), 9)

    def test_bin_search4(self):
        list_val =[0,1,2,3]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), None)
if __name__ == "__main__":
        unittest.main()

    
