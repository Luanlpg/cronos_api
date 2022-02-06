# syntax=docker/dockerfile:1
FROM python:3.8-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN apk --update add gcc build-base freetype-dev libpng-dev openblas-dev
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
COPY . /code/
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh