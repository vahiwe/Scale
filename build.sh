#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py collectstatic
# python manage.py makemigrations job
python manage.py migrate