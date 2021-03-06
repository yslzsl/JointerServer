"""JointerServer URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin

from cmdb.views import *

urlpatterns = [
    url(r'^index$', index),
    url(r'^index/$', index),
    url(r'^index/ajaxServerDetail/', ajaxServerDetail),
    url(r'^index/ajaxOptionLogs/', ajaxOptionLogs),
    url(r'^index/ajaxServerRemark/', ajaxServerRemark),
    url(r'^index/export/', export),
    url(r'^management$', index),
    url(r'^management/upload/$', upload),
    url(r'^management/modify/$', modify),
    url(r'^management/ajaxServerDelete/$', ajaxServerDelete),
]