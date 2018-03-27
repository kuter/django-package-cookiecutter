# -*- coding: utf-8 -*-
from django.test import TestCase
from ..models import {{cookiecutter.model}}


class {{cookiecutter.model}}Tests(TestCase):

    u"""Test class for {{cookiecutter.model}}."""

    def setUp(self):
        u"""Setup for {{cookiecutter.model}}."""
        self.obj = {{cookiecutter.model}}()

    def test_isinstance(self):
        u"""Test for isinstance method."""
        self.assertTrue(isinstance(self.obj, {{cookiecutter.model}}))
