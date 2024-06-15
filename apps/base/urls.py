
from django.urls import path, include
from .views import base_view

urlpatterns = [
    path('base_views/', base_view, name='base_views'),
]