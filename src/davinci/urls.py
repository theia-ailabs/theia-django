from django.urls import path

from . import views

urlpatterns = [
    path('/davinci', views.index, name='index'),
]
