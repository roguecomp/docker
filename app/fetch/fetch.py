from yahoo_fin import stock_info
import requests
import redis
from time import sleep
from flask import Flask

r = redis.Redis(host='redis', port=6379, db=0)
app = Flask(__name__)

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
    
    tick = 0

    from datetime import datetime, time 

    # GETTING HISTORICAL DATA
    # data = {}

    # data[stock] = stock_info.get_data(stock, start_date='01/01/2019')
    # #print(data[stock]['open']['2021-01-21'])

    # for date, price in data[stock]['open'].items():
    #     date = str(date)[:-9]
    #     r.hset(stock+'_all', str(date), str(price))

    prices = {}
    prices.popitem()
    while 1:
        if in_between(datetime.now().time(), time(14, 30), time(21, 00)):
        # if in_between(datetime.now().time(), time(00, 00), time(23, 59)):
            """
                US Stock Market is OPEN!!!

                -> time in container amancevice/pandas:alpine is in UTC
                -> Market is open 9:30am - 4:00pm ET == 2:30pm - 9:00pm UTC
            """
            tick += 1
            stock_price = stock_info.get_live_price(stock)
            prices[tick] = stock_price

            r.hmset("PRICE", prices)
            r.hset(stock, 'price', stock_price)
            #r.set(stock, stock_price)
            # time = str(datetime.now())[11:-7]
            # r.hset(stock, 'time', time)
        else:
            # resetting variables
            tick = 0

            print("Market Closed")
            
            sleep(5) 

update_stock()

def get_stock_history(stock='TSLA'):
    """getting stocks historical data 

    Args:
        stock (str, optional): Name of the stock. Defaults to 'TSLA'.
    """

    history = {}
    history[stock] = stock_info.get_data(stock, start_date='01/01/2019')

    return history 

stock = 'TSLA'

@app.route('/')
def welcome_page():
    return 'WELCOME!!!'


@app.route('/graph')
def update():

    history = get_stock_history(stock) 
    return history

if __name__ == '__main__':
    app.run(debug=True , host='0.0.0.0', port=5000)