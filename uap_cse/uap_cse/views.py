from django.shortcuts import render
from django.shortcuts import get_object_or_404

from clubs.models import Club
from faculty.models import Faculty
from faculty.scholar_api import get_or_cache_best_papers
from academics.models import fact_and_figures

def home(request):
    facts = fact_and_figures.objects.all()
    return render(request, 'home.html', {
        "facts":facts
    })

def faculty(request):
    facultys = Faculty.objects.all().order_by('sl')
    return render(request, 'faculty/faculty.html', {
        'facultys' : facultys
    })

def test(request):
    clubs = Club.objects.all()
    return render(request, 'clubs/test.html', {"clubs": clubs})

def club_detail(request):
    return render(request, 'clubs/club_detail.html')

def gallery(request):
    return render(request, 'hard_html/gallery.html')

def error(request):
    return render(request, 'hard_html/errorPage.html')

def tester(request):
    return render(request, 'tester.html')



