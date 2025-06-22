from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LectureViewSet, EnrollmentViewSet
from . import views_frontend

router = DefaultRouter()
router.register('courses', CourseViewSet, basename='courses')
router.register('lectures', LectureViewSet, basename='lectures')
router.register('enrollments', EnrollmentViewSet, basename='enrollments')

urlpatterns = [
    path('', include(router.urls)),
    path('courses-page/', views_frontend.course_list_view, name='course_list'),
    path('lectures-page/', views_frontend.lecture_list_view, name='lecture_list'),
    path('enrollments-page/', views_frontend.enrollment_list_view, name='enrollment_list'),
    path('enroll/<int:course_id>/', views_frontend.enroll_course, name='enroll-course'),
]