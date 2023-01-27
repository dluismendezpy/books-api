FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /books/
COPY requirements.txt /books/
COPY scripts/create-db.sh /books/

RUN pip install --no-cache-dir -r requirements.txt
COPY . /books/

COPY scripts/create-db.sh /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/create-db.sh
