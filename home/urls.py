from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("publications", views.research, name="publications"),
    path("paper/<int:paperID>/<str:paperTitle>", views.paper),
    path("patient-experience", views.reviews),
    path("contact", views.contact),
    path("send/", views.send),
]