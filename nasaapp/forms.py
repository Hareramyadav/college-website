from dataclasses import fields
from django.forms import ModelForm
from .models import *

class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'