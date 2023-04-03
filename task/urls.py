from django.urls import path

from task.views import TaskListView, TagsListView, TaskCreateView, TaskUpdateView, TaskDeleteView, complete_undo_task

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagsListView.as_view(), name="tag-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("<int:pk>/complete_undo_task/", complete_undo_task, name="complete-undo-task")
]

app_name = "task"
