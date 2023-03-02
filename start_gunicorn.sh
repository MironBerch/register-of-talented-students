#!/bin/bash
.venv/Scripts/activate
exec gunicorn - c 'C:/Users/MIRON/Documents/GitHub/register_of_talented_students/register_of_talented_students/gunicorn_config.py' config.wsgi