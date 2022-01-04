# PhotoStats
Statistics about photos


## Open ToDos
- trips/events model

## Configuration
1. Remove 'example_' from files in [config](./config/)
2. Maintain variables in there.

## Run
```
$ cd photostats
$ python manage.py runserver
```

### Hints
- Logging goes to 'BASE_DIR / 'import.log'


### Access
- [Admin overview](http://localhost:8000/admin/)
- [Image list](http://localhost:8000/images/)

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

#### Debugging Django
Seems to be a bit buggy. Make sure to not only install VSCode extension "Python" but also "Python Extension Pack".
Restarting Code and killing all breakpoints seems also to help (sometimes).