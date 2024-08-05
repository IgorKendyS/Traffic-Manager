from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import GoogleAdsData, FacebookAdsData
from .models import FacebookAccount
from .forms import FacebookAccountForm
from .services import import_facebook_data

@login_required
def import_facebook_data_view(request):
    if request.method == 'POST':
        success = import_facebook_data(request.user)
        if success:
            messages.success(request, "Dados do Facebook importados com sucesso!")
        else:
            messages.error(request, "Houve um erro ao importar os dados do Facebook.")
    return redirect('metrics')

@login_required
def metrics_view(request):
    platform = request.GET.get('platform', 'google')  # 'google' é o padrão
    
    if platform == 'facebook':
        data = FacebookAdsData.objects.all().order_by('-data')
        columns = ['Data', 'Campanha', 'Alcance', 'Impressões', 'Gasto', 'Cliques no Link']
    else:
        data = GoogleAdsData.objects.all().order_by('-day')
        columns = ['Data', 'Campanha', 'Cliques', 'Impressões', 'Custo', 'Conversões']

    context = {
        'data': data,
        'columns': columns,
        'current_platform': platform
    }
    return render(request, 'metrics.html', context)

@login_required
def add_facebook_account(request):
    if request.method == 'POST':
        form = FacebookAccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            account.save()
            return redirect('list_facebook_accounts')
    else:
        form = FacebookAccountForm()
    return render(request, 'add_facebook_account.html', {'form': form})

@login_required
def list_facebook_accounts(request):
    accounts = FacebookAccount.objects.filter(user=request.user)
    return render(request, 'list_facebook_accounts.html', {'accounts': accounts})