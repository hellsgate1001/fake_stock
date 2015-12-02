from datetime import datetime, timedelta

from formula import geometric_mean
from stocks import SAMPLE, Stock
from trade_generator import generate_trades

def main():
    # Generate fake trades for each stock
    trade_stocks = []
    for ss in SAMPLE:
        trade_stocks.append(Stock(ss))

    for trade_stock in trade_stocks:
        trade_stock.trades = []
        fake_trades = generate_trades()
        for fake_trade in fake_trades:
            trade_stock.record_trade(
                fake_trade[0], fake_trade[1], fake_trade[2], fake_trade[3]
            )

    # Calculate the stock price based on trades in the last 15 minutes
    # Calculate the All Share Index
    since = datetime.now() + timedelta(minutes=-15)
    prices = []
    for trade_stock in trade_stocks:
        print 'Stock price for %s: %s' % (
            trade_stock.symbol,
            trade_stock.calculate_stock_price(since)
        )
        prices.extend(trade_stock.all_prices())
    print 'GBCE All Share Index: %s' % geometric_mean(prices)

if __name__ == '__main__':
    main()
