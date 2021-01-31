import redis
from time import sleep
from datetime import datetime, time

stock = 'TSLA'

r = redis.Redis(host='redis', port=6379, db=0)

def get_stock_history(stock='TSLA'):
    """getting stocks historical data 

    Args:
        stock (str, optional): Name of the stock. Defaults to 'TSLA'.
    """

    data = r.hgetall(stock+'_all')

    for key, val in dict(data).items():
        key = key.decode('UTF-8')
        val = float(val.decode('UTF-8'))
        data[key] = val

    return data

data = get_stock_history(stock)

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

prices = []
times = []
while 1:
    if bool(in_between(datetime.now().time(), time(14, 30), time(21, 00))):
        price = r.hget(stock, 'price')
        price = float(price)
        print("Current Price: {}".format(price))
        prices.append(price)
        time = r.hget(stock, 'time').decode('UTF-8')
        times.append(time)

        sleep(1)
    else:
        # Market is closed
        print("closed")
        prices = []
        times = []
        sleep(5)

