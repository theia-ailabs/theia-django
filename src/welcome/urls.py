from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.index, name='index'),
]
