from django import forms
from .models import Notice, Course

class NoticeBoardForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'image', 'description']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'title', 'description', 'credit', 'year', 'semester']

class Fact_Figure_Form(forms.ModelForm):
    class Meta:
        model = fact_and_figures
        fields = ['title', 'description']

class PrerequisiteForm(forms.ModelForm):
    class Meta:
        model = Prerequisite
        fields =['prerequisite']