from django.apps import AppConfig


class {{cookiecutter.project_slug|title}}Config(AppConfig):
    name = '{{cookiecutter.project_slug}}'
    verbose_name = u'{{cookiecutter.project_name}}'
