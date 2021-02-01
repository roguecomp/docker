FROM pypy:3.7-slim

RUN pip3 install flask redis
COPY main.py /flask.py

ENTRYPOINT ["pypy", "flask.py"]