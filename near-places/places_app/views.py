from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,"index.html")

def pond(request):
    return render(request,"pond.html")

def skatingarea(request):
    return render(request,"skatingarea.html")

def fitnesstraining(request):
    return render(request,"fitnesstraining.html")

def entrance(request):
    return render(request,"entrance.html")

def towerclub(request):
    return render(request,"towerclub.html")
