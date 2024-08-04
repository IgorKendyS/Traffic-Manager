from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard_view(request):
    context = {
        'username': request.user.username
    }
    return render(request, 'dashboard.html', context)
