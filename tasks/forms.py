from .models import tasks
from django.forms import ModelForm
from django import forms

class Taskform(forms.ModelForm):

    class Meta:
        model = tasks
        fields = '__all__'
