from django import forms
from django.forms import ModelForm
from todolist.models import Task

class TaskForm(ModelForm):
    title = forms.CharField(max_length=255)
    description = forms.CharField(max_length=500)

    class Meta:
        model = Task
        exclude = ('user', 'date')
        fields = ('title', 'description')