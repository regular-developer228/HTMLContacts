from django.shortcuts import render

def home(request):
    return render(request, "list.html")

def add(request):
    return render(request, "create.html")

def abt(request):
    return render(request, "about.html")