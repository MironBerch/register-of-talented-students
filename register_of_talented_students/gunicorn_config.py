command = '/home/miron/Documents/register_of_talented_students/.venv/bin/gunicorn' #'/home/www/code/project/env/bin/gunicorn'DJANGO_SETTINGS_MODULE
pythonpath = '/home/miron/Documents/register_of_talented_students/register_of_talented_students' # path tp project'/home/www/code/project/project'
bind = '127.0.0.1:8000'
workers = 5  #2 * col yader + 1
user = 'miron'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=config.settings'