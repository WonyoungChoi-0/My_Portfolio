from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'portfolio/index.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def industry(request):
    return render(request, 'portfolio/industry.html')

def resume(request):
    return render(request, 'portfolio/resume.html')
