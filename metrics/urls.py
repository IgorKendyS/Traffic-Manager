from django.urls import path
from . import views

urlpatterns = [
    path('metrics/', views.metrics, name='metrics'),
]