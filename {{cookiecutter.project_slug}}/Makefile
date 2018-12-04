run:
	python manage.py runserver 8000

test:
	coverage run manage.py test

migrate:
	python manage.py makemigrations {{cookiecutter.project_slug}}
	python manage.py migrate

dist:
	python setup.py sdist

.PHONY: docs check flake8 isort pydocstyle bandit test
docs:
	cd docs/ && $(MAKE) clean && $(MAKE) html

coverage: test
	coverage report
	coverage html

flake8:
	@echo 'Check flake8 ..'
	flake8 --output-file=flake8.log

isort:
	@echo 'Check isort ..'
	isort -rc -c --skip migrations

pydocstyle:
	@echo 'Check docstring style ..'
	pydocstyle

bandit:
	@echo 'Check bandit ..'
	bandit -r .

check: flake8 isort pydocstyle bandit
