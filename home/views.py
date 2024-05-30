from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def tasks(request):
    return render(request, 'tasks.html')
