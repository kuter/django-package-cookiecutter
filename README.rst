django-package-cookiecutter
===========================

Django third-party app cookiecutter template for Django 2.1

Installation
------------

.. code:: bash

    $ mkvirtualenv blog
    $ pip install cookiecutter

Creating app template
---------------------

.. code:: bash

    $ cookiecutter https://github.com/kuter/django-package-cookiecutter
    full_name [user]: kuter        
    project_name [Sample Django app]: Blog
    project_slug [blog]: blog
    Select open_source_license
    1 - MIT license
    2 - BSD license
    3 - ISC license
    4 - Apache Software License 2.1
    5 - GNU General Public License v3
    6 - Not open source
    Choose from 1, 2, 3, 4, 5, 6 [1]: 1


Run Django project
------------------

.. code:: bash
    
    $ cd blog
    $ pip install -r requirements/local.txt
    $ python manage.py makemigrations blog
    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ python manage.py runserver

Generate documentation and run with your Web browser
----------------------------------------------------

.. code:: bash

   $ make docs
   $ xdg-open docs/build/html/index.html

Run tests and generate coverage
-------------------------------

.. code:: bash

   $ make coverage
   $ xdg-open htmlcov/index.html

To check against python coding standards run
--------------------------------------------

.. code:: bash

   $ make check
