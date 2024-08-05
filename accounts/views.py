from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def my_view(request):
    return HttpResponse('Hello, World!')

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
