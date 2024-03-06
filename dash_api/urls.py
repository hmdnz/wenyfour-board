from django.urls import path
from . import views

urlpatterns = [
    path('dash', views.dashboard, name='dashboard'),
    # Add other URL patterns as needed
]
