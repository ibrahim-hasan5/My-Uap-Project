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