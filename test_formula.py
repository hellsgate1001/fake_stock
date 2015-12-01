import unittest

from formula import (common_dividend_yield, preferred_dividend_yield, pe_ratio,
    geometric_mean, stock_price)


class TestFormulae(unittest.TestCase):
    def test_common_yield_success(self):
        dividend = 10
        ticker = 100
        self.assertEqual(
            common_dividend_yield(dividend, ticker),
            0.1
        )

    def test_common_yield_dividend_error(self):
        self.assertRaises(TypeError, common_dividend_yield, '10', 100)

    def test_common_yield_ticker_error(self):
        self.assertRaises(TypeError, common_dividend_yield, 10, '100')

    def test_preferred_yield_success(self):
        dividend = 0.1
        par = 100
        ticker = 100
        self.assertEqual(
            preferred_dividend_yield(dividend, par, ticker),
            0.1
        )

    def test_preferred_yield_dividend_error(self):
        self.assertRaises(TypeError, preferred_dividend_yield, '0.1', 100, 100)

    def test_preferred_yield_par_error(self):
        self.assertRaises(TypeError, preferred_dividend_yield, 0.1, '100', 100)

    def test_preferred_yield_ticker_error(self):
        self.assertRaises(TypeError, preferred_dividend_yield, 0.1, 100, '100')

    def test_pe_ratio_success(self):
        dividend = 10
        ticker = 100
        self.assertEqual(
            pe_ratio(dividend, ticker),
            10
        )

    def test_pe_ration_dividend_error(self):
        self.assertRaises(TypeError, pe_ratio, '10', 100)

    def test_pe_ration_ticker_error(self):
        self.assertRaises(TypeError, pe_ratio, 10, '100')

    def test_geometric_mean_success(self):
        prices = [2, 8]
        self.assertEqual(
            geometric_mean(prices),
            4
        )

    def test_geometric_mean_error(self):
        prices = [2, 8, '9', 5]
        self.assertRaises(TypeError, geometric_mean, prices)

    def test_stock_price_success(self):
        trades = (
            (60, 15),
            (40, 5),
            (100, 10)
        )
        self.assertEqual(
            stock_price(trades),
            70
        )

    def test_stock_price_error(self):
        trades = (
            (60, 15),
            (40, '5'),
            (100, 10)
        )
        self.assertRaises(TypeError, stock_price, trades)


if __name__ == '__main__':
    unittest.main()
