from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

def home(request):
    contacts = Contact.objects.all()
    return render(request, "list.html", {'contacts':contacts})

def add(request):
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
        return render(request, "create.html", {'form':form})

def abt(request):
    return render(request, "about.html")

def edit(request):
    pass

def delete(request):
    pass