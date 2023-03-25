from django.urls import path

from . import views

urlpatterns = [
    path('davinci/', views.davinciEX, name='davinci'),
]
