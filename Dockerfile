FROM python:3.8.6

ENV APP_HOME /app
WORKDIR $APP_HOME

RUN apt-get update
RUN apt-get install -y libsndfile1-dev
RUN apt-get install -y mecab libmecab-dev mecab-ipadic-utf8

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY app .

CMD exec gunicorn --bind :$PORT --workers 1 --timeout 0 --threads 8 app:app