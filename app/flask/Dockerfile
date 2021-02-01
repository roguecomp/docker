FROM pypy:3.7-slim

RUN pip3 install flask redis
COPY main.py /main.py

ENTRYPOINT ["pypy", "main.py"]