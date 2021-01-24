FROM pypy:3.7-slim 

RUN pip3 install 
COPY fetch.py /var/lib/pandas/fetch.py
ENTRYPOINT [ "pypy", "fetch.py" ]