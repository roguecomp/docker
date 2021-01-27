FROM amancevice/pandas:alpine

RUN pip3 install requests yahoo_fin redis beautifulsoup4
COPY fetch.py /var/lib/pandas/fetch.py
ENTRYPOINT [ "python3", "/var/lib/pandas/fetch.py" ]