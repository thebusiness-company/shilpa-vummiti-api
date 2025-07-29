#!/bin/sh

echo "Running Django setup..."

python manage.py collectstatic --noinput
python manage.py migrate

exec gunicorn yourproject.wsgi:application --bind 0.0.0.0:8000
