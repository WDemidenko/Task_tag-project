from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from task.forms import TaskCreatingForm
from task.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "task/index.html"

    def get_queryset(self):
        self.queryset = Task.objects.order_by("task_is_done", "-created")
        return self.queryset


class TagsListView(generic.ListView):
    model = Tag


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreatingForm
    success_url = reverse_lazy("task:task-list")
    template_name = "task/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskCreatingForm
    success_url = reverse_lazy("task:task-list")
    template_name = "task/task_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task:task-list")


def complete_undo_task(request, pk):
    task = Task.objects.get(pk=pk)
    if task.task_is_done:
        task.task_is_done = False
    else:
        task.task_is_done = True
    task.save()

    return HttpResponseRedirect(reverse("task:task-list"))
