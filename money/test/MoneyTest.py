from money.src.Dollar import Dollar
import unittest

class MoneyTest(unittest.TestCase):

    def test_multiplication(self):

        five = Dollar(5)
        product = five.times(2)
        self.assertEqual(10, product.amount)

        product = five.times(3)
        self.assertEqual(15, product.amount)

    def test_equality(self):
        self.assertTrue(Dollar(5) == Dollar(5))