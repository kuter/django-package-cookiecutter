run:
	python manage.py runserver

test:
	python manage.py test

coverage:
	coverage run manage.py test && coverage html

.PHONY: docs
docs:
	cd docs && make clean && make html

clean:
	find . -type d -name __pycache__ -exec rm -r {} \;
	rm -r docs/build/*
	rm -r htmlcov/
	rm .coverage
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.swp' -delete
	find . -type d -name .ropeproject -exec rm -r {} \;

