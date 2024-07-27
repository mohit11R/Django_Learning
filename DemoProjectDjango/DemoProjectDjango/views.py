from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Welcome to Mohit World!")
    return render(request,"index.html")

def about(request):
    return HttpResponse("Welcome to Mohit World!: Building Websites")