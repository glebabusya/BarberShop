from django.urls import path, include
from os import environ

urlpatterns = []

if environ.get("BUILD_TYPE") == "DEV":
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
