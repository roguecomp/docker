FROM pypy:3.7-slim

RUN pip3 install requests yahoo_fin redis beautifulsoup4
COPY fetch.py /fetch.py
ENTRYPOINT [ "python3", "/fetch.py" ]