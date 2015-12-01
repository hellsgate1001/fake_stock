import unittest

from stocks import Stock


class TestStock(unittest.TestCase):
    def test_stock_create_success(self):
        stock = self._valid_stock()

        self.assertEqual(stock.symbol, 'TEA')
        self.assertEqual(stock.type, 'Common')
        self.assertEqual(stock.last_dividend, 0)
        self.assertIsNone(stock.fixed_dividend)
        self.assertEqual(stock.par_value, 100)

    def test_stock_create_symbol_error(self):
        with self.assertRaises(TypeError):
            stock = Stock([9, 'Common', 0, None, 100])

    def test_stock_create_type_error(self):
        with self.assertRaises(TypeError):
            stock = Stock(['TEA', 9, 0, None, 100])

    def test_stock_create_type_value_error(self):
        with self.assertRaises(ValueError):
            stock = Stock(['TEA', 'Unique', 0, None, 100])

    def test_stock_create_last_dividend_error(self):
        with self.assertRaises(TypeError):
            stock = Stock(['TEA', 9, 0.2, None, 100])

    def test_stock_create_fixed_dividend_error(self):
        with self.assertRaises(TypeError):
            stock = Stock(['TEA', 9, 0, 'None', 100])

    def test_stock_create_par_value_error(self):
        with self.assertRaises(TypeError):
            stock = Stock(['TEA', 9, 0, None, '100'])

    def test_calculate_dividend_yield_common(self):
        stock = self._valid_stock()
        self.assertEqual(stock.calculate_dividend_yield(10, 100), 0.1)

    def test_calculate_dividend_yield_preferred(self):
        stock = self._valid_stock()
        stock.type = 'Preferred'
        self.assertEqual(stock.calculate_dividend_yield(0.1, 100, 100), 0.1)

    def test_calculate_stock_price_error(self):
        stock = self._valid_stock()
        self.assertRaises(
            TypeError,
            stock.calculate_stock_price,
            'yesterday'
        )

    def _valid_stock(self):
        return Stock(['TEA', 'Common', 0, None, 100])


if __name__ == '__main__':
    unittest.main()
