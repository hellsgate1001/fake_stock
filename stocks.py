from datetime import datetime

from formula import Formulae

SAMPLE = [
    ['TEA', 'Common', 0, None, 100],
    ['POP', 'Common', 8, None, 100],
    ['ALE', 'Common', 23, None, 60],
    ['GIN', 'Preferred', 8, 0.02, 100],
    ['JOE', 'Common', 13, None, 250],
]

trades = []


class Stock(object):
    def __init__(self, stock, *args, **kwargs):
        if stock[1].lower() not in ['common', 'preferred']:
            raise ValueError("Trade type must be one of 'common' or 'preferred'")
        super(Stock, self).__init__()
        (self.symbol, self.type, self.last_dividend, self.fixed_dividend,
            self.par_value = stocks)
        self.formulae = Formulae

    def calculate_dividend_yield(self):
        if self.type.lower() == 'common':
            return self.formulae.common_dividend_yield(
                dividend, ticker
            )
        elif self.type.lower() == 'preferred':
            return self.formulae.preferred_dividend_yield(
                dividend, par, ticker
            )

    def calculate_pe_ratio(self, dividend, ticker_price):
        return self.formulae.pe_ratio(dividend, ticker_price)

    def record_trade(self, quantity, trade_type, price):
        if not isinstance(quantity, (int, long)):
            raise TypeError('Quantity must be an integer.')
        if trade_type.lower() not in ['buy','sell']:
            raise ValueError("Trade type must be one of 'buy' or 'sell'.")
        if not isinstance(price, float):
            raise TypeError('Price must be a float.')

        trade = [
            datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
            quantity,
            trade_type,
            price
        ]
        trades.append(trade)

    def calculate_stock_price(self, since=None):
        if since is not None and not isinstance(since, datetime):
            raise TypeError('Since must be a datetime.')

        calculation_trades = []
        for trade in trades:
            if since is None or trade[0] >= since:
                calculation_trades.append(trade)

        return self.formulae.stock_price(calculation_trades)

    def calculate_all_share_index(self):
        prices = []
        for trade in trades:
            prices.append(trade[3])
        return self.formulae.geometric_mean(prices)
