from django.urls import path

from . import views


urlpatterns = [
    path('', views.{{cookiecutter.project_slug|title}}ListView.as_view(), name='{{cookiecutter.project_slug}}-list'),
    path('<int:pk>/', views.{{cookiecutter.project_slug|title}}DetailView.as_view(), name='{{cookiecutter.project_slug}}-detail')
]
