from django.urls import path, include
{% if cookiecutter.rest_framework == 'yes' %}from rest_framework.routers import DefaultRouter{% endif %}

from . import views
{% if cookiecutter.rest_framework == 'yes' %}
from .apiviews import {{cookiecutter.model}}ViewSet

router = DefaultRouter()
router.register('{{cookiecutter.model.lower()}}s', {{cookiecutter.model}}ViewSet, base_name='blogs')
{% endif %}

urlpatterns = [
    path('', views.{{cookiecutter.model}}ListView.as_view(), name='{{cookiecutter.model.lower()}}-list'),
    path('<int:pk>/', views.{{cookiecutter.model}}DetailView.as_view(), name='{{cookiecutter.model.lower()}}-detail'),
    {% if cookiecutter.rest_framework == 'yes' %}path(r'api/', include(router.urls)),{% endif %}
]
