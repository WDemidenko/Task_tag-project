from django.urls import reverse_lazy
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
    form_class = TaskCreatingForm
    success_url = reverse_lazy("task:task-list")
    template_name = "task/task_form.html"
