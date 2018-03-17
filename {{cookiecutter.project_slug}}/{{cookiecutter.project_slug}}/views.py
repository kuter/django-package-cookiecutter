from django.views.generic import DetailView, ListView

from .models import {{cookiecutter.project_slug|title}}


class {{cookiecutter.project_slug|title}}DetailView(DetailView):

    """{{cookiecutter.project_slug|title}}ListView documentation."""

    model = {{cookiecutter.project_slug|title}}


class {{cookiecutter.project_slug|title}}ListView(ListView):

    """{{cookiecutter.project_slug|title}}ListView documentation."""

    model = {{cookiecutter.project_slug|title}}
