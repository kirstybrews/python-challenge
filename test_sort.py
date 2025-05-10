import unittest
from sort import sort

class TestSort(unittest.TestCase):
    def test_bulky_and_heavy(self):
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")
        self.assertEqual(sort(50, 50, 150, 20), "REJECTED")
        self.assertEqual(sort(50, 50, 151, 20), "REJECTED")

    def test_heavy(self):
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")
        self.assertEqual(sort(10, 10, 10, 21), "SPECIAL")

    def test_bulky(self):
        self.assertEqual(sort(101, 101, 101, 10), "SPECIAL")
        self.assertEqual(sort(150, 50, 50, 10), "SPECIAL")
        self.assertEqual(sort(50, 150, 50, 10), "SPECIAL")
        self.assertEqual(sort(50, 50, 150, 10), "SPECIAL")

    def test_standard(self):
        self.assertEqual(sort(10, 10, 149, 10), "STANDARD")

if __name__ == '__main__':
    unittest.main()