from datetime import datetime, timedelta
import random

from stocks import SAMPLE, Stock

def generate_trades(number=100):
    fake_trades = []

    start_date = datetime.now() + timedelta(hours=-1)

    for i in range(number):
        qty = random.randint(1, 500)
        trade_type = random.choice(['buy', 'sell'])
        ticker_price = random.randint(1, 1000)
        trade_date = generate_random_date(start_date)
        fake_trades.append([qty, trade_type, ticker_price, trade_date])

    return fake_trades

def generate_random_date(start=None):
    if start is None:
        start = datetime.now() + timedelta(hours=-1)

    end = datetime.now()
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds()))
    )
