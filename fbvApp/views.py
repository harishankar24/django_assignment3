from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm


def courseList(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses':courses})


def createCourse(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'create.html', {'form':form})


def deleteCourse(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('/')


def updateCourse(request, id):
    course = Course.objects.get(id=id)
    form = CourseForm(instance=course)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'update.html', {'form':form})




