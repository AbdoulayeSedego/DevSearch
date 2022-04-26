from dataclasses import field
from django.forms import ModelForm


from django.forms import ModelForm
from .models import Project

class projectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'demo_link', 'source_link', 'tags']