from django.db import models


class {{cookiecutter.model}}(models.Model):

    """{{cookiecutter.model}} documentation."""

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "{{cookiecutter.model}}"
        verbose_name_plural = "{{cookiecutter.model}}s"
