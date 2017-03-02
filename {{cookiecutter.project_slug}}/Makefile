run:
	python manage.py runserver 8000

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.swp' -delete

test:
	python manage.py test

coverage:
	coverage run manage.py test
	coverage report

html:
	coverage html

dist:
	python setup sdist

.PHONY: docs
docs:
	cd docs/ && $(MAKE) clean && $(MAKE) html

migrate:
	python manage.py makemigrations articles
	python manage.py migrate
