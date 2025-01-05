import time
import requests as req
from bs4 import BeautifulSoup as soup

def main():
    # main URL
    base_url = 'https://finance.yahoo.com/quote/'
    
    # our tickers
    stocks = [ 'AAPL', 'GOOG', 'MSFT', 'penjaber' ]

    for ticker in stocks:
        stockpage = req.get(base_url+ticker)    
        print(f'[-] Status code: {stockpage.status_code}')
        if stockpage.status_code == 200:
            # ok
            source = stockpage.text
            parsedpage = soup(source, 'html.parser')
            try:
                price = parsedpage.find('fin-streamer', attrs = {'data-symbol': ticker}, class_ = 'livePrice').text
            except:
                price = 0
            print(f'[-] Ticker {ticker} has price {price}')
            print(f'\t[-] {base_url+ticker}')

            try:
                delta = parsedpage.find('fin-streamer', attrs = {'data-symbol': ticker}, class_ = 'priceChange').text
            except:
                delta = 0
            print(f'[-] Ticker {ticker} has delta {delta}')
            
        else:
            print(f'[x] Request to page {base_url+ticker} failed, status code: {stockpage.status_code} ')
        time.sleep(1)

    #print(f'[-] Last page resp.: {stockpage.text}')
    
    return

if __name__ == '__main__':
    main()