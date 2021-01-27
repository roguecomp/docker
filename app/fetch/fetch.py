from bs4 import BeautifulSoup as bs
from yahoo_fin import stock_info
import requests
import redis
from time import sleep

# def get_articles(url):
#     page_url = url 
#     page = requests.get(page_url)
#     soup = bs(page.content, 'html.parser')

#     u = soup.find_all('a')
#     url = []
#     for i in u:
#         for word in str(i).split(' '):
#             if(word[:7]=='href="/'):
#                 end = word.find('html"')
#                 url.append(word[7:end+4])

#     urls = []
#     for i in url:
#         urls.append(page_url + i)

#     urls = list(set(urls))
#     return urls 
#     urls = urls[-2:]
#     url = ""
#     for url in urls:
#     """repeat for every article found
#     """
#         page = requests.get(url)
#         soup = bs(page.content, 'html.parser')
#         a = soup.find_all('p')

r = redis.Redis(host='redis', port=6379, db=0)

def in_between(now, start, end):
    """Finding out if given time is between two ranges

    Args:
        now (time): given time
        start (time): start time (lower bound)
        end (time): end time (upper time)

    Returns:
        bool: Checks if time is between upper and lower bounds
    """
    if start <= end:
        return start <= now < end
    else: # over midnight e.g., 23:30-04:15
        return start <= now or now < end

def update_stock(stock="TSLA"):
    
    price = []
    tick = 0

    from datetime import datetime, time 

    while 1:
        if in_between(datetime.now().time(), time(14, 30), time(21, 00)):
            """
                US Stock Market is OPEN!!!
                time in container amancevice/pandas:alpine is in UTC
                Market is open 9:30am - 4:00pm ET == 2:30pm - 9:00pm UTC
            """
            tick += 1
            sleep(5)
            stock_price = stock_info.get_live_price(stock)
            price.append(stock_price)
            
            if(tick % 720 == 0):
                # Add stock prices to redis database every hour
                # the market is open
                r.set(stock, price)
        else:
            # resetting variables
            price = []
            tick = 0

            print("Market Closed")
            sleep(5)

update_stock()