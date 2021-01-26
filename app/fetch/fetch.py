from yahoo_fin import stock_info
import redis
import time

print("done.............................")

r = redis.Redis(host='redis', port=6379, db=0)

while 1:
    time.sleep(1)
    stock_price = stock_info.get_live_price('AAPL')
    curr_time = time.ctime()[11:-5] # storing current time in 24 hr format
    print("Stock Price: {}".format(stock_price))
    r.set(curr_time, stock_price)
