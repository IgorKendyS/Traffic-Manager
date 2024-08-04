from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from memory_profiler import profile

@profile
def my_view(request):
    data = [x for x in range(100000)]
    return HttpResponse('Hello, World!')

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
