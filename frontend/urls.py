from django.urls import path
from . import views


urlpatterns = [
    path('', views.frontend, name='frontend'),
]