FROM python:3.8-slim-buster

WORKDIR /scoring

COPY scoring .
RUN pip3 install -r requirements.txt


CMD [ "python3", "flask_app.py"]