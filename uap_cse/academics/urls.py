# results/urls.py
from django.urls import path
from . import views
from .views import routine_view
urlpatterns = [
    path('curriculum/', views.curriculum_view, name='curriculum'),
    path('admission-results/', views.admission_result_view, name='admission_results'),
    path('routine/', views.routine_view, name='routine_view'),
    path('waiver/', views.waiver, name='waiver'),
    path('exam_routine/', views.exam_routine_view, name='exam_routine'),
    path('missions/', views.mission_view, name='mission_view'),
    path('academic-calendar/', views.academic_calendar_view, name='academic_calendar_view'),
    path('icpc-event/', views.icpc_event_view, name='icpc_event_view'),
path('notice-board/', views.notice_board_view, name='notice_board'),
    path('notice/<int:notice_id>/', views.notice_detail_view, name='notice_detail'),
    path('course', views.course, name='course'),
    path('edit-course', views.edit_course, name='edit-course'),
    path('add-course', views.add_course, name='add-course'),
    path('update-course/<int:pk>', views.update_course, name='update-course'),
    path('delete-course/<int:pk>', views.delete_course, name='delete-course'),
]
