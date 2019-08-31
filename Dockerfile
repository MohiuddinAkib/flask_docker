FROM python:3.6.8

ARG FLASK_RUN_PORT

LABEL author="md akib"

WORKDIR /usr/src/app

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE ${FLASK_RUN_PORT}

ENTRYPOINT [ "flask", "run" , "--host" ]

CMD [ "0.0.0.0" ]