from django.urls import path

from . import views

urlpatterns = [
    path('', views.{{cookiecutter.model}}ListView.as_view(),
         name='{{cookiecutter.model.lower()}}-list'),
    path('<int:pk>/', views.{{cookiecutter.model}}DetailView.as_view(),
         name='{{cookiecutter.model.lower()}}-detail'),
]
