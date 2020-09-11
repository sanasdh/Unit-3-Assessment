from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView
from .models import Task
from .forms import TaskForm


def index(request):
    sum = 0
    tasks = Task.objects.all()
    task_form = TaskForm()
    for task in tasks:
        sum = sum+task.time
    return render(request, "main_app/task_list.html", {"tasks": tasks, "task_form": task_form, "sum": sum})


def add_task(request):
    form = TaskForm(request.POST)
    print("form")
    print(form)

    if form.is_valid():
        obj = Task()
        obj.person = form.cleaned_data['person']
        obj.description = form.cleaned_data['description']
        obj.time = form.cleaned_data['time']
        obj.save()
    return HttpResponseRedirect("/")


class TaskDelete(DeleteView):
    model = Task
    success_url = '/'
