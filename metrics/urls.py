from django.urls import path
from . import views
from .views import metrics_view

urlpatterns = [
    path('', metrics_view, name='metrics'),
    path('facebook-accounts/add/', views.add_facebook_account, name='add_facebook_account'),
    path('facebook-accounts/', views.list_facebook_accounts, name='list_facebook_accounts'),
    path('import-facebook-data/', views.import_facebook_data_view, name='import_facebook_data'),
]