import redis
from time import sleep

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

while 1:
    price = r.hget(stock, 'price')
    time = r.hget(stock, 'time')
    
    
    sleep(1)

