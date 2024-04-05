import yfinance as yf
from config import *

def analyze_stock():
    # get stock data from yfinance
    ticker = yf.Ticker(SYMBOL)
    hist = ticker.history(period=PERIOD, interval=INTERVAL)

    volume_condition_met = True
    drop_condition_met = True

    # check stock data
    for i in range(1, len(hist)):
        # calculate the rate of increase in volume
        volume_increase = hist['Volume'][i] / hist['Volume'][i-1] if hist['Volume'][i-1] > 0 else 0
        # calculate the rate of stock price decline
        price_drop = (hist['Close'][i-1] - hist['Low'][i]) / hist['Close'][i-1] if hist['Close'][i-1] > 0 else 0

        # evaluate conditions
        if volume_increase <= VOLUME_RATE:
            volume_condition_met = False
        if price_drop <= DROP_RATE:
            drop_condition_met = False

    # push notification
    if volume_condition_met and drop_condition_met:
        print(f"{SYMBOL}: push notification")
    else:
        print(f"{SYMBOL}: don't push notification")
