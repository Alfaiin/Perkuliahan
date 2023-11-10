
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'register.html')
def about(request):
    return HttpResponse('<marquee>Ini Adalah Halaman About</marquee>')