# -*- coding: utf-8 -*-
from django.test import TestCase
from ..models import {{cookiecutter.project_slug|title}}


class {{cookiecutter.project_slug|title}}Tests(TestCase):

    u"""Test class for {{cookiecutter.project_slug|title}}."""

    def setUp(self):
        u"""Setup for {{cookiecutter.project_slug|title}}."""
        self.obj = {{cookiecutter.project_slug|title}}()

    def test_isinstance(self):
        u"""Test for isinstance method."""
        self.assertTrue(isinstance(self.obj, {{cookiecutter.project_slug|title}}))
