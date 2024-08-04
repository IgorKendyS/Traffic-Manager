from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView
from dashboard.views import dashboard_view  # Importação da view do dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard_view, name='index'),  # URL raiz para o dashboard
    path('accounts/', include('accounts.urls')),  # Prefixo para URLs de contas
    path('metrics/', include('metrics.urls')),  # Prefixo para URLs de métricas
    path('campaigns/', include('campaigns.urls')),  # Prefixo para URLs de campanhas
    path('pages/', include('pages.urls')),  # Prefixo para URLs de páginas
    path('logout/', LogoutView.as_view(), name='logout'),  # URL de logout
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),  # URL de login
]
