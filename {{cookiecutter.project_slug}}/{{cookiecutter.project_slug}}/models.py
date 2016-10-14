# -*- coding: utf-8 -*-
from django.db import models


class {{cookiecutter.project_slug|title}}(models.Model):

    u""" {{cookiecutter.project_slug|title}} documentation. """

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "{{cookiecutter.project_slug|title}}"
        verbose_name_plural = "{{cookiecutter.project_slug|title}}s"
