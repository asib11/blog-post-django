# Django

A Django starter template as per the docs: https://docs.djangoproject.com/en/5.0/intro/tutorial01/

## Admin site

to make super user, first do

    python3 manage.py makemigrations
    python3 manage.py migrate

create super user

    python3 manage.py createsuperuser

## database and migration

    python3 manage.py makemigrate
    python3 manage.py sqlmigrate <app name> <migrate initial file number>
    python3 manage.py migrate