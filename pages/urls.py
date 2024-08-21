from django.contrib import admin
from django.urls import path, include
from .views import Home, About
urlpatterns = [
    path('about/', About.as_view(), name='about'),
    path("", Home.as_view(),name='home'),

]
