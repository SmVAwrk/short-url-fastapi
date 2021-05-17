FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /usr/src/app

EXPOSE 8080

WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x entrypoint.sh

