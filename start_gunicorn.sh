#!/bin/bash
source /home/miron/Documents/register_of_talented_students/.venv/bin/activate
exec gunicorn -c '/home/miron/Documents/register_of_talented_students/register_of_talented_students/gunicorn_config.py' config.wsgi