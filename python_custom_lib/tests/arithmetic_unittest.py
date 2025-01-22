import unittest2 as unittest
from src.arithmetic import Arithmetic

class TestArithmetic(unittest.TestCase):
    def setUp(self):
        self.arithmetic = Arithmetic(5, 10)

    def test_add_positive_numbers(self):
        self.arithmetic.a = 5
        self.arithmetic.b = 10
        result = self.arithmetic.add()
        self.assertEqual(result, 15)

    def test_add_negative_numbers(self):
        self.arithmetic.a = -5
        self.arithmetic.b = -10
        result = self.arithmetic.add()
        self.assertEqual(result, -15)

    def test_add_zero(self):
        self.arithmetic.a = 0
        self.arithmetic.b = 0
        result = self.arithmetic.add()
        self.assertEqual(result, 0)

    def test_add_positive_and_negative_number(self):
        self.arithmetic.a = 10
        self.arithmetic.b = -5
        result = self.arithmetic.add()
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()