from django.test import TestCase

from ..models import {{cookiecutter.model}}


class {{cookiecutter.model}}Tests(TestCase):

    """Test class for {{cookiecutter.model}}."""

    def setUp(self):
        """Setup for {{cookiecutter.model}}."""
        self.obj = {{cookiecutter.model}}()

    def test_isinstance(self):
        """Test for isinstance method."""
        self.assertTrue(isinstance(self.obj, {{cookiecutter.model}}))
