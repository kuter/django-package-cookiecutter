"""
Installation
============

Getting the code
----------------

.. code:: bash

    $ pip install {{cookiecutter.project_slug}}

Prerequisites
-------------

Make sure that ``'django.contrib.staticfiles'`` is `set up properly
<https://docs.djangoproject.com/en/stable/howto/static-files/>`_ and add
``'{{cookiecutter.project_slug}}'`` to your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = [
        # ...
        'django.contrib.staticfiles',
        # ...
        '{{cookiecutter.project_slug}}',
    ]

    STATIC_URL = '/static/'

URLconf
-------

Add the {{cookiecutter.project_name}}'s URLs to your project's URLconf as follows::

    from django.conf import settings
    from django.conf.urls import include, url

    urlpatterns = [
        url(r'^{{cookiecutter.project_slug}}/', include('{{cookiecutter.project_slug}}.urls')),
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
default_app_config = '{{cookiecutter.project_slug}}.apps.{{cookiecutter.project_slug|title}}Config'
