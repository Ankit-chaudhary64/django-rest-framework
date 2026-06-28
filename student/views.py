from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def student(request):
    students=[{"name": "Alice", "age": 20}, {"name": "Bob", "age": 22}]
    return HttpResponse(students)