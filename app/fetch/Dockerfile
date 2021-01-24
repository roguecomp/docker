FROM pypy:3.7-slim 

RUN pip3 install yahoo_fin
COPY fetch.py /var/lib/pandas/fetch.py
ENTRYPOINT [ "python3", "fetch.py" ]