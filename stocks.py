from datetime import datetime
from operator import itemgetter

from formula import (common_dividend_yield, preferred_dividend_yield,
    pe_ratio, geometric_mean, stock_price)

SAMPLE = [
    ['TEA', 'Common', 0, None, 100],
    ['POP', 'Common', 8, None, 100],
    ['ALE', 'Common', 23, None, 60],
    ['GIN', 'Preferred', 8, 0.02, 100],
    ['JOE', 'Common', 13, None, 250],
]


class Stock(object):
    trades = []

    def __init__(self, stock, *args, **kwargs):
        if not isinstance(stock[0], str):
            raise TypeError('Please provide the stock symbol as a string.')
        if not isinstance(stock[1], str):
            raise TypeError('Please provide the trade type as a string.')
        if stock[1].lower() not in ['common', 'preferred']:
            raise ValueError("Trade type must be one of 'common' or 'preferred'")
        if not isinstance(stock[2], (int, long)):
            raise TypeError('Last dividend must be a valid integer.')
        if stock[3] is not None and not isinstance(stock[3], (float, int, long)):
            raise TypeError('Fixed dividend must be a valid number if it is provided.')
        if not isinstance(stock[4], (int, long)):
            raise TypeError('Par Value must be a valid integer.')

        super(Stock, self).__init__()
        self.symbol, self.type, self.last_dividend, self.fixed_dividend, self.par_value = stock

    def calculate_dividend_yield(self, dividend, ticker, par=None):
        if self.type.lower() == 'common':
            return common_dividend_yield(
                dividend, ticker
            )
        elif self.type.lower() == 'preferred':
            return preferred_dividend_yield(
                dividend, par, ticker
            )

    def calculate_pe_ratio(self, dividend, ticker_price):
        return pe_ratio(dividend, ticker_price)

    def record_trade(self, quantity, trade_type, ticker_price, trade_dt=None):
        if not isinstance(quantity, (int, long)):
            raise TypeError('Quantity must be an integer.')
        if trade_type.lower() not in ['buy','sell']:
            raise ValueError("Trade type must be one of 'buy' or 'sell'.")
        if not isinstance(ticker_price, (float, int, long)):
            raise TypeError('Price must be a valid number.')

        if trade_dt is None:
            trade_dt =datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        trade = [
            trade_dt,
            quantity,
            trade_type,
            ticker_price
        ]
        self.trades.append(trade)

    def calculate_stock_price(self, since=None):
        if since is not None and not isinstance(since, datetime):
            raise TypeError('Since must be a datetime.')

        calculation_trades = []
        # This loop is run against the list of trades which has been sorted
        # in reverse date order so that we can exit the loop as soon as we reach
        # a trade which has taken place outside the 'since' window
        for trade in sorted(self.trades, key=itemgetter(0), reverse=True):
            # trade_datetime = datetime.strptime(trade[0], '%Y-%m-%dT%H:%M:%S')
            if since is None or trade[0] >= since:
                calculation_trades.append([trade[3], trade[1]])

            if since is not None and trade[0] < since:
                break

        return stock_price(calculation_trades)

    def all_prices(self):
        return [t[3] for t in self.trades]
