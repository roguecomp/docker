FROM amancevice/pandas:alpine

RUN pip3 install requests yahoo_fin redis
COPY fetch.py /var/lib/pandas/fetch.py
ENTRYPOINT [ "python3", "fetch.py" ]