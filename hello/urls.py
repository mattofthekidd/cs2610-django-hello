from django.conf.urls import urls
from . import views

urlpatters = [
    url(r'^$', views.index, name='index'),
    ]