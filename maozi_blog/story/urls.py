from django.urls import path
from . import views

urlpatterns = [
    path('', views.story, name='story')
]
