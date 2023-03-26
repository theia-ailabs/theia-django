from django.urls import path

from . import views

urlpatterns = [
    path('theia/', views.theia, name='theia'),
]
