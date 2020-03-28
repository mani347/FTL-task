from django.urls import path, include
from . import views

urlpatterns = [
    path('show-data', views.view, name='show_data')
]
