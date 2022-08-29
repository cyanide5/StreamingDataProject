FROM python:3.9-slim
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN apt-get install postgresql-dev

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --deploy --system

CMD exec gunicorn --bind 0.0.0.0:5000 --workers 1 --worker-class uvicorn.workers.UvicosssrnWorker  --threads 8 app.main:app

CMD gunicorn --bind 0.0.0.0:5000 run:app