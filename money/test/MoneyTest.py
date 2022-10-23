from money.src.Dollar import Dollar
import unittest

class MoneyTest(unittest.TestCase):

    def test_multiplication(self):

        five = Dollar(5)
        five.times(2)
        self.assertEqual(10, five.amount)

        five.times(3)
        self.assertEqual(15, five.amount)