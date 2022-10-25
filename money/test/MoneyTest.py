from money.src.Money import Money
from money.src.Bank import Bank
from money.src.Sum import Sum
import unittest

class MoneyTest(unittest.TestCase):

    def test_multiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five.times(2))
        self.assertEqual(Money.dollar(15), five.times(3))

    def test_equality(self):
        self.assertTrue(Money.dollar(5) == Money.dollar(5))
        self.assertFalse(Money.dollar(5) == Money.dollar(6))
        self.assertFalse(Money.dollar(5) == None)
        self.assertFalse(Money.franc(5) == Money.dollar(5))

    def test_currency(self):
        self.assertEqual("USD", Money.dollar(1).currency())
        self.assertEqual("CHF", Money.franc(1).currency())

    def test_simple_additon(self):
        five = Money.dollar(5)
        sum_exp = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(sum_exp, "USD")
        self.assertEqual(Money.dollar(10), reduced)

    def test_plus_returns_sum(self):
        five = Money.dollar(5)
        sum_exp = five.plus(five)
        self.assertEqual(five, sum_exp.augend)
        self.assertEqual(five, sum_exp.addend)

    def test_reduce_sum(self):
        sum_exp = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(sum_exp, "USD")
        self.assertEqual(Money.dollar(7), result)

    def test_reduce_money(self):
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result = bank.reduce(Money.dollar(1), "USD")
        self.assertEqual(Money.dollar(1), result)

    def test_reduce_money_different_currency(self):
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result = bank.reduce(Money.franc(2), "USD")
        self.assertEqual(Money.dollar(1), result)

    def test_mixed_addition(self):
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result = bank.reduce(five_bucks.plus(ten_francs), "USD")
        self.assertEqual(Money.dollar(10), result)

    def test_sum_plus_money(self):
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        sum_result = Sum(five_bucks, ten_francs).plus(five_bucks)
        result = bank.reduce(sum_result, "USD")
        self.assertEqual(Money.dollar(15), result)

    def test_sum_times(self):
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        sum_result = Sum(five_bucks, ten_francs).times(2)
        result = bank.reduce(sum_result, "USD")
        self.assertEqual(Money.dollar(20), result)

    def test_plus_same_currency_returns_money(self):
        sum_result = Money.dollar(1).plus(Money.dollar(1))
        self.assertTrue(isinstance(sum_result, Money))