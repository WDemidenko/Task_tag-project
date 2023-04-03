from django.urls import path

from task.views import TaskListView, TagsListView, TaskCreateView, TaskUpdateView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagsListView.as_view(), name="tag-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
]

app_name = "task"
