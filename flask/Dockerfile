FROM python:3.7.4-slim

MAINTAINER Duohong "duohong@duohong.com"

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app

EXPOSE 5000/tcp
ENTRYPOINT ["python"]
CMD ["app.py"]
