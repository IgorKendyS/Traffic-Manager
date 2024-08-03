from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('metrics.urls')),
    path('campaigns/', include('campaigns.urls')),
    path('', include('pages.urls')),
]