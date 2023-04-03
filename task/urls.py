from django.urls import path

from task.views import TaskListView, TagsListView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagsListView.as_view(), name="tag-list")
]

app_name = "task"
