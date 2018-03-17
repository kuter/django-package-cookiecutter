django-plugin-template-cookiecutter
===================================

Django third-party app cookiecutter template for Django 2.0.x

Installation:

.. code:: bash

    $ mkvirtualenv blog
    $ pip install cookiecutter

Creating app template:

.. code:: bash

    $ cookiecutter https://github.com/kuter/django-plugin-template-cookiecutter                                                                                                                                                     
    full_name [user]: kuter        
    project_name [Sample Django app]: Blog
    project_slug [blog]: blog
    Select open_source_license
    1 - MIT license
    2 - BSD license
    3 - ISC license
    4 - Apache Software License 2.0
    5 - GNU General Public License v3
    6 - Not open source
    Choose from 1, 2, 3, 4, 5, 6 [1]: 1

Run Django project:

.. code:: bash
    
    $ cd blog
    $ pip install -r requirements/local.txt
    $ python manage.py makemigrations blog
    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ python manage.py runserver
