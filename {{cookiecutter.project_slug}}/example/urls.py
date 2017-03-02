"""example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import debug_toolbar

from django.conf import settings
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.views.generic.base import RedirectView, TemplateView
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^docs/$', RedirectView.as_view(url='index.html')),
    url(r'^coverage/$', RedirectView.as_view(url='index.html')),
    url(r'^docs/(?P<path>.*)', serve, {'document_root': 'docs/build/html'}),
    url(r'^coverage/(?P<path>.*)', serve, {'document_root': 'htmlcov'}),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
]
