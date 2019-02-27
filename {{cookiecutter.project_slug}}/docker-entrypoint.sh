#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
pip install gunicorn
gunicorn --workers 2 --bind 0.0.0.0:8000 --timeout=600 pay2win.wsgi:application
