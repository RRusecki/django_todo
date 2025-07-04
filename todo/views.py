from django.shortcuts import render
from .models import Task
from django.contrib.auth.decorators import login_required
from . import views

@login_required
def task_list(request):
    task = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'todo/task_list.html', {'task': tasks})