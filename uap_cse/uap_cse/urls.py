"""
URL configuration for uap_cse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('faculty/', views.faculty, name='faculty'),
    path('faculty/<int:pk>/', views.faculty_detail, name='faculty_detail'),
    path('undergraduate/', views.undergraduate, name='undergraduate'),
    path('graduate/', views.graduate, name='graduate'),
    path('tuition/', views.tuition, name='tuition'),
    path('why_cse/', views.why_cse, name='why_cse'),
    path('clubs/', views.clubs, name='clubs'),
    path('gallery/', views.gallery, name='gallery'),
    path('club_detail/', views.club_detail, name='club_detail'),
    path('', include('faculty.urls')),
    path('others/', include(('others.urls', 'others'), namespace='others')),
    path('tester/',views.tester,name='tester'),
    path('error/',views.error,name='error'),
    path('aca/',include('academics.urls')),
    path('test/',views.test,name='test'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)