# urls_frontend.py

from django.urls import path
from . import views_frontend
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('homepage/', views_frontend.homepage, name='homepage'),
    path('courses-page/', views_frontend.course_list_view, name='course_list'),
    path('lectures-page/<int:course_id>/', views_frontend.lecture_list_view, name='lecture_list'),
    path('enrollments-page/', views_frontend.enrollment_list_view, name='enrollment_list'),
    path('login-page/', views_frontend.login, name='login'),
    path('search-courses/', views_frontend.search_courses, name='search_courses'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
