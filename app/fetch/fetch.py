from yahoo_fin import stock_info
import requests
import redis
from time import sleep
from flask import Flask
from datetime import datetime, time

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
    else: 
        return start <= now or now < end

def get_stock_history(stock='TSLA'):
    """getting stocks historical data 

    Args:
        stock (str, optional): Name of the stock. Defaults to 'TSLA'.
    """

    history = stock_info.get_data(stock, start_date='01/01/2019')

    return history 

stock = 'TSLA'
history = get_stock_history(stock) 
# r.hmset('history', history)

@app.route('/')
def welcome_page():
    """Welcome Page

    Returns:
        website_payload: returns html file which can be viewed in browser
    """
    return 'WELCOME!!!'

@app.route('/graph')
def update():

    # if in_between(datetime.now().time(), time(14, 30), time(21, 00)):
    if in_between(datetime.now().time(), time(0, 00), time(23, 59)):
        """
        # US Stock Market is OPEN!!!

        -> time in container amancevice/pandas:alpine is in UTC
        -> Market is open 9:30am - 4:00pm ET == 2:30pm - 9:00pm UTC
        """

        stock_price = stock_info.get_live_price(stock)
        return str(stock_price)
    else:
        # Market is Closed
        return 'Market Closed!'

if __name__ == '__main__':
    app.run(debug=True , host='0.0.0.0', port=5000)