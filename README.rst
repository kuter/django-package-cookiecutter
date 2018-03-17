django-package-cookiecutter
===========================

Django third-party app cookiecutter template for Django 1.8.x

Installation:

.. code:: bash

    $ mkvirtualenv testapp
    $ pip install cookiecutter

Creating app template:

.. code:: bash

    $ cookiecutter -c 1.8.x https://github.com/kuter/django-package-cookiecutter
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

Usage:

.. code:: bash

    $ make run
    $ make test
    $ make docs
    $ make coverage
