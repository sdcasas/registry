from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields =  '__all__'
        widgets = {
            'students': FilteredSelectMultiple('Estudiantes', False),
        }
