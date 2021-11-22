from django.shortcuts import render
from .models import Task
from .forms import TaskForm

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def quadratic(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Введені невірні дані!'
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/quadratic.html')

def newton(request):
    return render(request, 'main/newton.html')
