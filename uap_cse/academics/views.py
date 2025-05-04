from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
# views.py
from django.shortcuts import render


from django.shortcuts import render
# views.py
from django.shortcuts import render, get_object_or_404
from .models import Notice,fact_and_figures


from django.http import HttpResponseForbidden
from functools import wraps
from faculty.models import AllowedEmail

def allowed_email_role_required(min_role='3'):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponseForbidden("You must be logged in.")

            try:
                allowed = AllowedEmail.objects.get(email=request.user.email)
                if int(allowed.role) >= int(min_role):
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponseForbidden("You do not have permission.")
            except AllowedEmail.DoesNotExist:
                return HttpResponseForbidden("You are not in the allowed list.")

        return _wrapped_view
    return decorator


def course(request):
    courses = Course.objects.all()
    prerequisites = Prerequisite.objects.all()
    return render(request, 'academics/course.html', {
        "courses":courses,
        "prerequisites":prerequisites,
    })
from .import forms

@allowed_email_role_required(min_role='3')
def add_fact(request):
    if request.method=="POST":
        form=forms.Fact_Figure_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edit-fact')
    else:
        form=forms.Fact_Figure_Form()
    return render(request,'forms.html',{
        "form":form,
    })

@allowed_email_role_required(min_role='3')
def update_fact(request, pk):
    fact = fact_and_figures.objects.get(pk=pk)
    if request.method == 'POST':
        form = forms.Fact_Figure_Form(request.POST or None, instance=fact)
        if form.is_valid():
            form.save()
            return redirect('edit-fact')
    else:
        form = forms.Fact_Figure_Form(instance=fact)
    return render(request, 'forms.html', {
        'form': form})
@allowed_email_role_required(min_role='3')
def delete_fact(request, pk):
    fact_and_figures.objects.get(pk=pk).delete()
    return redirect('edit-fact')

@allowed_email_role_required(min_role='3')
def edit_course(request):
    courses = Course.objects.all()
    prerequisites = Prerequisite.objects.all()
    return render(request, 'academics/edit_course.html', {
        "courses":courses,
        "prerequisites":prerequisites,
    })
@allowed_email_role_required(min_role='3')
def edit_fact(request):
    facts = fact_and_figures.objects.all()
    return render(request, 'academics/edit_fact.html', {
        "facts":facts
    })

from .import forms

@allowed_email_role_required(min_role='3')
def add_course(request):
    if request.method=="POST":
        form=forms.CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edit-course')
    else:
        form=forms.CourseForm()
    return render(request,'forms.html',{
        "form":form,
    })

@allowed_email_role_required(min_role='3')
def update_course(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == 'POST':
        form = forms.CourseForm(request.POST or None, instance=course)
        if form.is_valid():
            form.save()
            return redirect('edit-course')
    else:
        form = forms.CourseForm(instance=course)
    return render(request, 'forms.html', {
        'form': form})
@allowed_email_role_required(min_role='3')
def delete_course(request, pk):
    Course.objects.get(pk=pk).delete()
    return redirect('edit-course')


@allowed_email_role_required(min_role='3')
def set_prerequisite(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == "POST":
        form = forms.PrerequisiteForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.course = course
            instance.save()
            return redirect('edit-course')
    else:
        form = forms.PrerequisiteForm()
    return render(request, 'forms.html', {
        "form": form,
    })