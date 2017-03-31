from django.conf.urls import include, url
from django.contrib import admin

urlpatters = [
    url(r'^hello/',include('hello.urls')),
    url(r'^admin/', admin.site.urls),
]