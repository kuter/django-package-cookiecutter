clean:
	find . -type d -name __pycache__ -exec rm -r {} \;
	rm -r docs/build/*
	rm -r htmlcov/
	rm .coverage
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.swp' -delete
	find . -type d -name .ropeproject -exec rm -r {} \;

runserver:
	python manage.py runserver

test:
	python manage.py test

coverage:
	coverage run manage.py test
	coverage html

docs:
	cd docs/
	make html
