from django import forms
from .models import  Course



class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'title', 'description', 'credit', 'year', 'semester']


class PrerequisiteForm(forms.ModelForm):
    class Meta:
        model = Prerequisite
        fields =['prerequisite']