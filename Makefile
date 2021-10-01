SHELL := /bin/bash

include .env

install:
	pipenv install

shell:
	python manage.py shell

serve:
	python manage.py runserver

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

superuser:
	python manage.py createsuperuser

test:
	python manage.py test

herokumigrate:
	heroku run python manage.py migrate