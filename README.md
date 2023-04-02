# Register of talented students [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

## Technologies:
- python 3.10
- Django 4
- SQLite
- Bootstrap 5
- docker 20.10
- docker-compose 1.20

## Start project:

### by using a computer
- Run this command - it redirects to the code directory
```
cd register_of_talented_students
```
- Run this command - it download requirements
```
pip install -r requirements.txt
```
- Run these commands - they create database
```
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
```
- Run this command - it create superuser
```
python manage.py createsuperuser
```
- Everything is done - now you can start the server
```
python manage.py runserver
```

### by using docker on local server
- Run this command - it redirects to the code directory
```
cd register_of_talented_students
```
- Run this command - it start docker compose
```
docker-compose up --build
```

### by using docker on production server
- Run this command - it redirects to the code directory
```
cd register_of_talented_students
```
- Run this command - it start docker compose on server
```
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build
```

## Documentation

- [Project documentation](./docs/README.md)