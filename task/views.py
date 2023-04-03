from django.shortcuts import render
from django.views import generic

from task.models import Task


class TaskListView(generic.ListView):
    model = Task
    template_name = "task/index.html"

    def get_queryset(self):
        self.queryset = Task.objects.order_by("task_is_done", "-created")
        return self.queryset
