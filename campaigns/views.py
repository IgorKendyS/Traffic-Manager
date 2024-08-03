from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CampaignForm

@login_required
def campaign_list(request):
    # Lógica para listar campanhas
    return render(request, 'campaigns/list.html')

@login_required
def campaign_create(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            # Salvar campanha
            return redirect('campaign_list')
    else:
        form = CampaignForm()
    return render(request, 'campaigns/create.html', {'form': form})