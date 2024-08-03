from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    # Lógica para obter métricas de diferentes plataformas
    return render(request, 'metrics.html')