from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm


def courseList(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses':courses})


def deleteCourse(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('/')