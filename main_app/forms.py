from django.forms import ModelForm
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        # fields = ['description', 'time']
        fields = "__all__"
