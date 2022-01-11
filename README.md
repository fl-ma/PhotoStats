# PhotoStats
Statistics about photos


## Open ToDos
- reports
    - compare report (timerange 1 vs timerange 2)
    - list number of photos next to chart
    - show selected directory in dropdownbox
    - change hover texts (e.g. to show totals next to percentage)
        - apperently works via attribute customdata:
            - https://stackoverflow.com/questions/59057881/python-plotly-how-to-customize-hover-template-on-with-what-information-to-show

- directories
    - support a tree structure in selection (see directoryTree.py for comments)
    - create an endpoint to list all images within one dir

- extend datamodel of camera to type (Phone, DSLR, DSLM, Owner)

## Configuration
1. Remove 'example_' from files in [config](./config/)
2. Maintain variables in there.

## Run
```
$ cd photostats
$ python manage.py runserver
```

### Use
- [Admin overview](http://localhost:8000/admin/)
- [Importer](http://localhost:8000/importer/)
- [Image list](http://localhost:8000/images/)
- [Directory list](http://localhost:8000/directories/)
- [Reports](http://localhost:8000/reports/)


### External access
When trying to access the application from a different computer:
- settings.py, add: ALLOWED_HOSTS = ['*']
- pythong manage.py runserver 0.0.0.0:8000

### Hints
- Logging goes to 'BASE_DIR / 'import.log'
- Reset database with 'python manage.py flush'

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