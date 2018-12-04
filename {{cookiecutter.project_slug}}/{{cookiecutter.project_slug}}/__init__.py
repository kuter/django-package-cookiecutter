"""
Installation
============

Getting the code
----------------

.. code:: bash

    $ pip install {{cookiecutter.project_slug}}

Prerequisites
-------------

Add ``'{{cookiecutter.project_slug}}'`` to your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = [
        '{{cookiecutter.project_slug}}',
    ]


URLconf
-------

Add the {{cookiecutter.project_name}}'s URLs to your project's URLconf as follows::

    from django.conf import settings
    from django.urls import include, url

    urlpatterns = [
        path(r'^{{cookiecutter.project_slug}}/', include('{{cookiecutter.project_slug}}.urls')),
    ]

Application
===========

Models
------

.. automodule:: {{cookiecutter.project_slug}}.models
    :members:
    :show-inheritance:

Views
-----

.. automodule:: {{cookiecutter.project_slug}}.views
    :members:
    :show-inheritance:

Templates
---------

.. program-output:: tree ../../{{cookiecutter.project_slug}}/templates/
"""
__version__ = '0.0.0'
