
import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import Course, Enrollment

BASE_API_URL = "http://127.0.0.1:8000"  # Adjust if hosted remotely

def course_list_view(request):
    response = requests.get(f"{BASE_API_URL}/courses/")
    courses = response.json() if response.status_code == 200 else []

    enrolled_course_ids = []
    if request.user.is_authenticated:
        enrollments = Enrollment.objects.filter(student=request.user).values_list('course_id', flat=True)
        enrolled_course_ids = list(enrollments)

    return render(request, 'frontend/courses.html', {
        'courses': courses,
        'enrolled_course_ids': enrolled_course_ids,
    })

def lecture_list_view(request, course_id):
    response = requests.get(f"{BASE_API_URL}/lectures/")
    all_lectures  = response.json() if response.status_code == 200 else []
    lectures = [lec for lec in all_lectures if lec.get('course') == course_id]
    return render(request, 'frontend/lectures.html', {'lectures': lectures})



@login_required
def enrollment_list_view(request):
    enrollments = Enrollment.objects.filter(student=request.user).select_related('course')
    courses = [enrollment.course for enrollment in enrollments]
    return render(request, 'frontend/enrollments.html', {'courses': courses})


def homepage(request):
    return render(request, 'frontend/homepage.html')


@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    Enrollment.objects.get_or_create(student=request.user, course=course)
    return redirect('lecture_list', course_id=course.id)




def login(request):
    return render(request, 'account/login_page.html')