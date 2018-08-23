{% if cookiecutter.rest_framework == 'yes' %}
from rest_framework import viewsets

from .models import {{cookiecutter.model}}
from .serializers import {{cookiecutter.model}}Serializer


class {{cookiecutter.model}}ViewSet(viewsets.ModelViewSet):
    queryset = {{cookiecutter.model}}.objects.all()
    serializer_class = {{cookiecutter.model}}Serializer
{% else %}
# Write app API views here.
{% endif %}
