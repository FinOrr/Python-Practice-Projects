'''
Use scrapy to get data from yahoo finance
Get the top 100 stocks by market cap
Append their ticket symbol and price to a csv file
Repeat this every minute
'''

import scrapy
import csv
import time
import datetime

def get_price(symbol):
    # Scrape the data from yahoo finance
    url = 'https://finance.yahoo.com/quote/{}'.format(symbol)
    response = scrapy.Request(url, callback=parse_data(), dont_filter=True)
    
def parse_data(response):
    # Parse the data from yahoo finance
    data = response.css('div.My(6px) Pos(r) smartphone_Mt(6px)')
    price = data.css('span.Trsdu(0.3s) ::text').extract_first()
    return price

def write_data(symbol, price):
    # Write the data to a csv file
    with open('stocks.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([symbol, price, datetime.datetime.now()])

def main():
    for i in range(5):
        # Store the symbols for the top 10 stocks by market cap from yahoo finance
        symbols = ["AAPL", "AMZN", "FB", "GOOGL", "MSFT", "NFLX", "TSLA", "TWTR", "V", "WMT"]
        for symbol in symbols:
            price = get_price(symbols[0])
            print(f"Found {symbol} at {price}.")
            write_data(symbol, price)

        time.sleep(60)
    print("Done...")
    exit()

if __name__ == "__main__":
    main()