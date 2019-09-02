## Install requirements

On OSX, needs:

1. `postgresql`
2. `openssl` (to build psycopg2) (should be some `export LDFLAGS=...` you need to run)

```
pipenv install
```

## Develop

```
python manage.py runserver
```

Generate migrations
```
python manage.py makemigrations
```

Run above
```
python manage.py migrate
```
