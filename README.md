# PhotoStats
Statistics about photos


## DEV setup
1. Setup VENV
```
python3 -m venv .venv
```

2. Setup DJANGO (not needed, only for doc)
    2.1 $ django-admin startproject photostats (not needed, only for doc)
    2.2 $ python manage.py startapp images (not needed, only for doc)
    2.3 $ python manage.py migrate
    2.4 $ python manage.py makemigrations images
    2.5 $ python manage.py createsuperuser

After changes to Models:
    2.5 $ python manage.py sqlmigrate images 0001
    2.6 $ python manage.py migrate

3. Configuration
3.1 Remove 'example_' from files in [config](.config/)
3.2 Maintain variables in there.


4. Run
```
$ cd photostats
$ python manage.py runserver
```

### Dependencies
See [./requirements.txt](./requirements.txt) 
Install with
```
$ pip install -r requirements.txt
```