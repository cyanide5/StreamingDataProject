FROM python:3

COPY requirements.txt ./

# Install production dependencies.
RUN set -ex; \
    pip install -r requirements.txt; \
    pip install gunicorn

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

ENV INSTANCE_UNIX_SOCKET: /cloudsql/majestic-trail-36070:us-central1:streaming-data-project
ENV INSTANCE_CONNECTION_NAME: majestic-trail-360708:us-central1:streamingpostgres
ENV DB_USER: streaming_admin
ENV DB_PASS: password
ENV DB_NAME: streaming_services

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app