FROM pypy:messenger

RUN pip3 install selenium requests redis
RUN apt update && apt install -y firefox-esr
WORKDIR /home
COPY main /home/main
COPY .credentials.json /home/.credentials.json
COPY .messenger_ids.json /home/.messenger_ids.json
COPY ./geckodriver /bin/geckodriver
ENTRYPOINT [ "./main" ]
