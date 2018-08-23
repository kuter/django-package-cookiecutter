{% if cookiecutter.rest_framework == 'yes' %}
from rest_framework import serializers

from .models import {{cookiecutter.model}}


class {{cookiecutter.model}}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {{cookiecutter.model}}
        fields = '__all__'
{% else %}
# Write app serializers here.
{% endif %}
