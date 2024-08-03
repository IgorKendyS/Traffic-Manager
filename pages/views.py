from django.shortcuts import render

def policies(request):
    return render(request, 'policies.html')

def terms(request):
    return render(request, 'terms.html')