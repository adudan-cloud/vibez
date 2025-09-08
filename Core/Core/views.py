from django.shortcuts import render

def home_view(request):
    return render(request, 'accounts/home.html')

def calendar(request):
    return render(request,'calendar.html')

