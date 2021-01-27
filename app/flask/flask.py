import redis
from time import sleep

r = redis.Redis(host='redis', port=6379, db=0)
print(r.get('TSLA'))
sleep(2)
