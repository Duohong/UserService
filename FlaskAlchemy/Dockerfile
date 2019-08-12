FROM python:3.7.4-slim

MAINTAINER Duohong "duohong@duohong.com"

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app

EXPOSE 5000/tcp
ENTRYPOINT ["python"]
CMD ["app.py"]
