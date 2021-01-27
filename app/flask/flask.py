import redis
from time import sleep

r = redis.Redis(host='redis', port=6379, db=0)
data = r.hgetall('TSLA_all')

for key, val in dict(data).items():
    key = key.decode('UTF-8')
    val = float(val.decode('UTF-8'))
    data[key] = val

print(data)
sleep(2)
