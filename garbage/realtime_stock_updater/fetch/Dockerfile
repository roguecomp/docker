FROM amancevice/pandas:alpine

RUN pip3 install requests yahoo_fin redis beautifulsoup4 flask
WORKDIR /var/lib/pandas
COPY fetch.py fetch.py
COPY templates templates
ENTRYPOINT [ "python3", "/var/lib/pandas/fetch.py" ]