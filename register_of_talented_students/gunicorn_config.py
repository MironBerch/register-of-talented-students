command = 'C:/Users/MIRON/Documents/GitHub/register_of_talented_students/.venv/Lib/site-packages/gunicorn' #'/home/www/code/project/env/bin/gunicorn'
pythonpath = 'C:/Users/MIRON/Documents/GitHub/register_of_talented_students/register_of_talented_students' # path tp project'/home/www/code/project/project'
bind = '127.0.0.1:8000'
workers = 1 #2 * col yader + 1
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=config.settings'