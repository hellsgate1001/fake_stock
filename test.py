import unittest

from formula import Formulae


class TestFormulae(unittest.TestCase):
    def setUp(self):
        self.formulae = Formulae()

    def test_common_yield(self):
        dividend = 10
        ticker = 100
        self.assertEqual(
            self.formulae.common_dividend_yield(dividend, ticker),
            0.1
        )

    def test_preferred_yield(self):
        dividend = 0.1
        par = 100
        ticker = 100
        self.assertEqual(
            self.formulae.preferred_dividend_yield(dividend, par, ticker),
            0.1
        )

    def test_pe_ratio(self):
        dividend = 10
        ticker = 100
        self.assertEqual(
            self.formulae.pe_ratio(dividend, ticker),
            10
        )

    def test_geometric_mean(self):
        prices = [2, 8]
        self.assertEqual(
            self.formulae.geometric_mean(prices),
            4
        )

    def test_stock_price(self):
        trades = (
            (60, 15),
            (40, 5),
            (100, 10)
        )
        self.assertEqual(
            self.formulae.stock_price(trades),
            70
        )


if __name__ == '__main__':
    unittest.main()
