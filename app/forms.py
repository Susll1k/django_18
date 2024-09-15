from django import forms
from django.forms import modelformset_factory
from .models import Task
from captcha.fields import CaptchaField

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']

TaskFormSet = modelformset_factory(Task, form=TaskForm, extra=2)

class NonModelTaskForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    completed = forms.BooleanField(required=False)
    captcha = CaptchaField() 


