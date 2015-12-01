class Formulae(object):
    def common_dividend_yield(self, last_dividend, ticker_price):
        return float(last_dividend) / ticker_price

    def preferred_dividend_yield(self, fixed_dividend, par_value, ticker_price):
        return (fixed_dividend * par_value) / ticker_price

    def pe_ratio(self, dividend, ticker_price):
        if not isinstance(dividend, (float, int, long)):
            raise TypeError('Dividend must be a valid  number.')
        if not isinstance(ticker_price, (float, int, long)):
            raise TypeError('Ticker price must be a valid number.')

        return float(ticker_price) / dividend

    def geometric_mean(self, prices):
        return reduce(lambda x, y: x * y, prices) ** (1.0 / len(prices))

    def stock_price(self, trades):
        ttl = 0
        qty = 0
        for trade in trades:
            if not isinstance(trade[0], (float, int, long)):
                raise TypeError('Trade price must be a valid number.')
            if not isinstance(trade[1], (int, long)):
                raise TypeError('Trade quantity must be a valid integer.')

            ttl += (trade[0] * trade[1])
            qty += trade[1]

        return float(ttl) / qty
