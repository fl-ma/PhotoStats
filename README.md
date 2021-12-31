# PhotoStats
Statistics about photos


## Configuration
3.1 Remove 'example_' from files in [config](.config/)
3.2 Maintain variables in there.

## Run
```
$ cd photostats
$ python manage.py runserver
```

## DEV setup

### VENV
```
python3 -m venv .venv
```

### DJANGO
(This is documentation only, not needed locally)
- $ django-admin startproject photostats (not needed, only for doc)
- $ python manage.py startapp images (not needed, only for doc)
- $ python manage.py migrate
- $ python manage.py createsuperuser

#### After changes to Models:
- $ python manage.py makemigrations <app>
- $ python manage.py sqlmigrate images 0001
- $ python manage.py migrate

### Dependencies
See [./requirements.txt](./requirements.txt), install with:
```
$ pip install -r requirements.txt
```