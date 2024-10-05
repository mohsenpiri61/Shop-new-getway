FROM python:3.10-slim-buster

LABEL maintainer="mopiry@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app


COPY ./requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

# # Remove files inside /usr/src/app
# RUN rm -f /usr/src/app/manage.py

COPY ./core .