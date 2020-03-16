from django.urls import path

from . import views

urlpatterns = [
    path('', views.amber_main, name='amber')
]
