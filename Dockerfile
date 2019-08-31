FROM python:3.6.8

LABEL author="md akib"

ARG FLASK_RUN_PORT

ARG FLASK_RUN_HOST

ENV FLASK_RUN_HOST=${FLASK_RUN_HOST}

WORKDIR /usr/src/app

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE ${FLASK_RUN_PORT}

ENTRYPOINT [ "flask", "run" , "--host" ]

CMD [ "0.0.0.0" ]