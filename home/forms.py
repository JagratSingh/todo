from django import forms
from django.forms import ModelForm

from .models import *

class TodoForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Title...', 'class':'input'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter Task...', 'class':'input'}))
    
    class Meta:
        model = ToDo
        fields = '__all__'