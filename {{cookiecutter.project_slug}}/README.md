[![build status](http://gitlab/{{cookiecutter.full_name}}/{{cookiecutter.project_slug}}/badges/master/build.svg)](http://gitlab/{{cookiecutter.full_name}}/{{cookiecutter.project_slug}}/commits/master)
[![coverage report](http://gitlab/{{cookiecutter.full_name}}/{{cookiecutter.project_slug}}/badges/master/coverage.svg)](http://gitlab/{{cookiecutter.full_name}}/{{cookiecutter.project_slug}}/commits/master)
=====
{{cookiecutter.project_name}}
=============================
Third-party app created with https://github.com/kuter/django-plugin-template-cookiecutter

Quick start
-----------
1. Add "{{cookiecutter.project_slug}}" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        '{{cookiecutter.project_slug}}',
    ]
2. Include the polls URLconf in your project urls.py like this::

    path('{{cookiecutter.project_slug}}/', include('{{cookiecutter.project_slug}}.urls')),

3. Run `python manage.py migrate` to create the {{cookiecutter.project_slug}} models.
4. Start the development server and visit http://127.0.0.1:8000/admin/
to create a {{cookiecutter.project_slug}} object (you'll need the Admin app enabled).
5. Visit http://127.0.0.1:8000/{{cookiecutter.project_slug}}/.
