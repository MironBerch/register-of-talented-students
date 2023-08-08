#!/bin/sh

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 0.1
done

echo "Postgres did run"

python manage.py collectstatic --no-input

python manage.py makemigrations

python manage.py migrate

exec "$@"
