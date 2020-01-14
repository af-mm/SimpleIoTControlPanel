FROM python:3.7

WORKDIR /SimpleIoTControlPanel

COPY app.py config.py requirements.txt ./
COPY static ./static
COPY templates ./templates

RUN pip3 install -r requirements.txt

ENV WEB_SEVER_PORT=1024 \
	MQTT_BROKER_HOST=localhost \
	MQTT_BROKER_PORT=1024

CMD [ "python3", "./app.py" ]
