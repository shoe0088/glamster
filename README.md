# glamster
A tool that analyzes stock price movements and notifies of risks in advance.

## Parameters
- symbol: Ticker symbol
- time_scale: Minute chart
- window_size: Number of data points to check
- volume_rate: Rate of increase in volume used for decision
- drop_rate: Rate of decrease in stock price used for decision

## Algorithm
- Obtain the most recent window_size number of stock prices for symbol
- Compare preceding and succeeding data to notify if the following conditions are met:
  - The rate of increase in volume exceeds volume_rate in all instances
  - The rate of decrease in stock price exceeds drop_rate in all instances
 
## Calculation Method
- Rate of increase in volume = Volume of succeeding data / Volume of preceding data
- Rate of decrease in stock price = (Closing price of preceding data - Low of succeeding data) / Closing price of preceding data

## How to get stock prices
Use Yahoo Finance API
