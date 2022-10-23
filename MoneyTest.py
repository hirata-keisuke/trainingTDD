from money.src.Dollar import Dollar
from money.src.Franc import Franc
import unittest

class MoneyTest(unittest.TestCase):

    def test_multiplication(self):
        five = Dollar(5)
        self.assertEqual(Dollar(10), five.times(2))
        self.assertEqual(Dollar(15), five.times(3))

    def test_equality(self):
        self.assertTrue(Dollar(5) == Dollar(5))
        self.assertFalse(Dollar(5) == Dollar(6))
        self.assertFalse(Dollar(5) == None)

    def test_franc_multiplication(self) :
        five = Franc(5)
        self.assertEqual(Franc(10), five.times(2))
        self.assertEqual(Franc(15), five.times(3))