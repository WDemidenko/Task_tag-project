from django import forms

from task.models import Task, Tag


class TaskCreatingForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"


class TagCreatingForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
