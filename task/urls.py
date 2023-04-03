from django.urls import path

from task.views import TaskListView, TagsListView, TaskCreateView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagsListView.as_view(), name="tag-list"),
    path("create/", TaskCreateView.as_view(), name="task-create")
]

app_name = "task"
