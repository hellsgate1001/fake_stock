def common_dividend_yield(last_dividend, ticker_price):
    if not isinstance(last_dividend, (int, long, float)):
        raise TypeError('Last dividend must be a valid number.')
    if not isinstance(ticker_price, (int, long, float)):
        raise TypeError('Ticker price must be a valid number.')

    return float(last_dividend) / ticker_price

def preferred_dividend_yield(fixed_dividend, par_value, ticker_price):
    if not isinstance(fixed_dividend, (int, long, float)):
        raise TypeError('Fixed dividend must be a valid number.')
    if not isinstance(par_value, (int, long, float)):
        raise TypeError('Par value must be a valid number.')
    if not isinstance(ticker_price, (int, long, float)):
        raise TypeError('Ticker price must be a valid number.')

    return (fixed_dividend * par_value) / ticker_price

def pe_ratio(dividend, ticker_price):
    if not isinstance(dividend, (float, int, long)):
        raise TypeError('Dividend must be a valid  number.')
    if not isinstance(ticker_price, (float, int, long)):
        raise TypeError('Ticker price must be a valid number.')

    return float(ticker_price) / dividend

def geometric_mean(prices):
    for price in prices:
        if not isinstance(price, (int, long, float)):
            raise TypeError('Prices must be a valid number.')

    return reduce(lambda x, y: x * y, prices) ** (1.0 / len(prices))

def stock_price(trades):
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
