from django.urls import path

from task.views import TaskListView, TagsListView, TaskCreateView, TaskUpdateView, TaskDeleteView, complete_undo_task, \
    TagCreateView, TagUpdateView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagsListView.as_view(), name="tag-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("<int:pk>/complete_undo_task/", complete_undo_task, name="complete-undo-task"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update", TagUpdateView.as_view(), name="tag-update"),
]

app_name = "task"
