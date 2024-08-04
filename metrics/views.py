from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import GoogleAdsData, FacebookAdsData

@login_required
def metrics_view(request):
    platform = request.GET.get('platform', 'google')  # 'google' é o padrão
    
    if platform == 'facebook':
        data = FacebookAdsData.objects.all().order_by('-date')
        columns = ['Data', 'Campanha', 'Alcance', 'Impressões', 'Gasto', 'Cliques no Link']
    else:
        data = GoogleAdsData.objects.all().order_by('-date')
        columns = ['Data', 'Campanha', 'Cliques', 'Impressões', 'Custo', 'Conversões']

    context = {
        'data': data,
        'columns': columns,
        'current_platform': platform
    }
    return render(request, 'metrics.html', context)