# Руководство по развёртыванию проекта на VPS сервере

Это краткое руководство по развёртыванию проекта на производственный сервере.

## Конфигурация VPS сервера

#### Минимальная конфигурация VPS сервера:
| Комплектующие | Характеристика |
| ------ | ------ |
| CPU | 1 × 2000 МГц |
| RAM | 1 Гб |
| Диск | 5 Гб |

#### Рекомендуемая конфигурация VPS сервера:
| Комплектующие | Характеристика |
| ------ | ------ |
| CPU | 2 × 2000 МГц |
| RAM | 4 Гб |
| Диск | 10 Гб |

## Развёртывание проекта

- Запустите эту команду - она установит все зависимости необходимые для развёртывания проекта
```sh
sudo apt-get install git docker docker-compose vim
```

- Запустите эту команду - она скачает проект с GitHub
```sh
git clone https://github.com/MironBerch/register_of_talented_students.git
```

- Запустите эту команду - она перенаправляет в каталог с кодом
```sh
cd register_of_talented_students
```

- Запустите эту команду - она создаст `.env` файл с помощью vim 
```sh
vim .env
```

- Пример `.env` файла
```dotenv
ENV=.env

# Project
SECRET_KEY=not-secure-key
DEBUG=0

# Postgres
POSTGRES_DB=db
POSTGRES_USER=db_user
POSTGRES_PASSWORD=db_user_pass
POSTGRES_HOST=db
POSTGRES_PORT=5432

# Celery
CELERY_BROKER_URL=redis://redis:6379
```

- Запустите эту команду - она запустит сайт 
```sh
docker-compose -f docker-compose.yml -f docker-compose-master.yml up --build -d
```

- Запустите эту команду - она просмотрит docker контейнеры
```sh
docker ps
```

- Пример ответа
```sh
| CONTAINER ID |                IMAGE                | ... 
| ------------ | ----------------------------------- | --- 
| e87ee7777e59 | register_of_talented_students-nginx | ...
| 9b9701f23e02 | register_of_talented_students-server   | ...
```

- Выберете CONTAINER ID IMAGE которого register_of_talented_students-server
- Запустите эту команду - она запустит bash внутри docker контейнера
```sh
docker exec -it <CONTAINER_ID> bash
```

- Или запустите эту команду — она запустит sh внутри docker контейнера
```sh
docker exec -it <CONTAINER_ID> sh
```

- Запустите эту команду - она создаст администратора внутри docker контейнера
```sh
python manage.py createsuperuser
```
