# PhotoStats
Statistics about photos


## Open ToDos
- reports
    - filters for reports
    - compare report (timerange 1 vs timerange 2)

- paths
    - always end with /
    - directories as own model
        - incl text
        - as tree structure?
        - own importer

- trips/events model
- extend datamodel of camera to type (Phone, DSLR, DSLM)

## Configuration
1. Remove 'example_' from files in [config](./config/)
2. Maintain variables in there.

## Run
```
$ cd photostats
$ python manage.py runserver
```

### External access
When trying to access the application from a different computer:
- settings.py, add: ALLOWED_HOSTS = ['*']
- pythong manage.py runserver 0.0.0.0:8000

### Hints
- Logging goes to 'BASE_DIR / 'import.log'
- Reset database with 'python manage.py flush'


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
- $ python manage.py makemigrations images
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