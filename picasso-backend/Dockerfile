from python:3.7

RUN mkdir -p /usr/local/app
WORKDIR /usr/local/app

COPY requirements.txt uwsgi.ini /usr/local/app/
RUN apt-get update && pip --no-cache-dir install -r requirements.txt

COPY app /usr/local/app/app
EXPOSE 8000
CMD ["uwsgi", "--ini", "uwsgi.ini"]
