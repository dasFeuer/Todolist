from django.shortcuts import render
from home.models import Task


def index(request):
    context = {'success': False}
    if request.method == "POST":
        # Handle the form
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()

    return render(request, 'index.html', context)

def tasks(request):
    return render(request, 'tasks.html')
