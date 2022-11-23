from django.shortcuts import render

# Create your views here.
def jinja_project(request):
    d={'name':'reshu'}
    return render(request,'jinja_project.html',d)
