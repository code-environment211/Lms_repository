from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Course, Lecture, Enrollment
from .serializer import CourseSerializer, LectureSerializer, EnrollmentSerializer
from LMS_Project.permissions import IsInstructorOrReadOnly
from rest_framework.exceptions import NotAuthenticated


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsInstructorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]  # Enforce login

    def get_queryset(self):
        user = self.request.user.id
        return Enrollment.objects.filter(student=user)

    def perform_create(self, serializer):
        serializer.save(student=self.request.user.id)

# ------------------------------------------------------------------------

