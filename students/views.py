from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.


def students(request):
    students=[
        {'stdid':1,'name':'John','branch':'CSE'},
    ]
    return HttpResponse(students)