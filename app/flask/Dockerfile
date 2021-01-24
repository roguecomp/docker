FROM pypy:3.7-slim

RUN pip3 install flask
COPY flask.py /flask.py

ENTRYPOINT ["pypy", "flask.py"]