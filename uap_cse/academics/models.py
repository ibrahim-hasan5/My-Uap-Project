from django.db import models

# Create your models here.

# models.py
from django.db import models


from ckeditor.fields import RichTextField
class fact_and_figures(models.Model):
    title = models.CharField(max_length=120)
    description = RichTextField (blank=True, null=True)

    def __str__(self):
        return self.title

from ckeditor.fields import RichTextField
class Course(models.Model):
    code = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    description = RichTextField(blank=True,null=True)
    credit = models.FloatField(default=0.0)
    YEAR = [
        ('1st','1st'),
        ('2nd','2nd'),
        ('3rd','3rd'),
        ('4th','4th'),
    ]
    SEMESTER = [
        ('1st','1st'),
        ('2nd','2nd'),
    ]
    year = models.CharField(max_length=15, choices = YEAR, null = True)
    semester = models.CharField(max_length=15, choices = SEMESTER, null = True)

    def __str__(self):
        return self.code

class Prerequisite(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null= True,
        related_name='main_course_prerequisites'
    )
    prerequisite = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='prerequisite_for_courses'
    )

    def __str__(self):
        return f'{self.course}--{self.prerequisite}'