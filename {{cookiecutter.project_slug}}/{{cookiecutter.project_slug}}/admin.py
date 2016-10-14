# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import {{cookiecutter.project_slug|title}}


admin.site.register({{cookiecutter.project_slug|title}})
