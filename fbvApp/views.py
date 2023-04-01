from django.shortcuts import render
from .models import Course
from .forms import CourseForm


def courseList(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses':courses})