# DigitalDiary - Back-end

> [!CAUTION]
> Thanks for caution

DigitalDiary back-end server uses Django with the Django REST framework.

## Quickstart

### Set virtual environment

The supported version of **Python** is **3.11** _or higher_.

```shell
python3.11 -m virtualenv venv
. ./venv/bin/activate
pip install -r requirements.txt
```

### Setting database

Project uses **PostgreSQL**

```shell
sudo -u postgres psql
```

```postgresql
CREATE DATABASE digital_diary;
CREATE USER digital_diary WITH ENCRYPTED PASSWORD 'YOUR_PASSWORD';
GRANT ALL PRIVILEGES ON DATABASE digital_diary TO digital_diary;
ALTER ROLE digital_diary CREATEDB; -- for testing
```

You need to create `.env` file:

```dotenv
POSTGRES_DB=digital_diary
POSTGRES_USER=digital_diary
POSTGRES_PASSWORD=YOUR_PASSWORD
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
DEBUG=true
SECRET_KEY=YOUR_SECRET_KEY
```

### Migrations and superuser

```shell
./manage.py migrate
./manage.py createsuperuser
```

### Running

```shell
./manage.py runserver --noreload 
```

### Deploy

Tested with:

- _Gunicorn_ WSGI
- _Nginx_ web server
