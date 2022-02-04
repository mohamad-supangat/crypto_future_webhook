from python:alpine3.15

MAINTAINER hantamkoding@gmail.com

COPY . /app
WORKDIR /app

RUN pip install pipenv

RUN pipenv install --system --deploy

CMD ["python", "app.py"]
