#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py initadmin
python manage.py loaddata fixtures.yaml
python manage.py runserver 0.0.0.0:8000
exec "$@"