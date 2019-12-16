FROM tiangolo/uwsgi-nginx-flask:python3.6

# Install flask-restful
RUN pip install flask-restful

# Install FDB (Firebird DB)
RUN pip install fdb

# Install Firebird DB client library
RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y libfbclient2

COPY ./app /app
