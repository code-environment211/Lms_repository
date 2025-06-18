from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LectureViewSet, EnrollmentViewSet

router = DefaultRouter()
router.register('courses', CourseViewSet, basename='courses')
router.register('lectures', LectureViewSet, basename='lectures')
router.register('enrollments', EnrollmentViewSet, basename='enrollments')

urlpatterns = [
    path('', include(router.urls))
]