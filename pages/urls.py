from django.urls import path
from . import views

urlpatterns = [
    path('policies/', views.policies, name='policies'),
    path('terms/', views.terms, name='terms'),
]