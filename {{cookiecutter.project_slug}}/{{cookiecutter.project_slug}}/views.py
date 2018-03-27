from django.views.generic import DetailView, ListView

from .models import {{cookiecutter.model}}


class {{cookiecutter.model}}DetailView(DetailView):

    """{{cookiecutter.model}}ListView documentation."""

    model = {{cookiecutter.model}}


class {{cookiecutter.model}}ListView(ListView):

    """{{cookiecutter.model}}ListView documentation."""

    model = {{cookiecutter.model}}
