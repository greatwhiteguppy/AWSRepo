# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import datetime
from .models import Course

# Create your views here.
def index(request):
    context = {
    'courses': Course.objects.all()
    # select * from Course like MySQL workbench
    }
    return render(request, "course_app/index.html", context)

def addcourse(request):
    # using ORM
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    # insert into course (name, description, created_at, updated_at) values (name, description)
    return redirect('/')


def remove(request, id):
    print "Removing a course!"
    if request.method == "POST":
        print request.POST
        deleted_course = Course.objects.get(id=id)
        print "This is the course we deleted:", deleted_course.id, "-", deleted_course.name

        deleted_course.delete()
        return redirect('/')

    if request.method == "GET":
        print request.GET
        context = {
            "course" : Course.objects.get(id=id)
        }
        return render(request, "course_app/remove.html", context)
