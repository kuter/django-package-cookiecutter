from django.apps import AppConfig


class {{cookiecutter.project_slug|title}}Config(AppConfig):  # noqa: D101
    name = '{{cookiecutter.project_slug}}'
    verbose_name = u'{{cookiecutter.project_name}}'
