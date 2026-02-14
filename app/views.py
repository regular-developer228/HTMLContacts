from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.db.models import Q

def home(request):
    contacts = Contact.objects.all()

    query = request.GET.get('q')
    results = []
    if query:
        contacts = Contact.objects.filter(
            Q(name__icontains=query) |
            Q(phone__icontains=query) |
            Q(mail__icontains=query)
        )

    return render(request, "list.html", {'contacts':contacts, 'query':query})

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

def edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm(instance=contact)
        return render(request, "create.html", {'form':form})

def delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('home')

def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Contact.objects.filter(
            Q(name__icontains=query) |
            Q(phone__icontains=query) |
            Q(mail__icontains=query)
        )
    return render(request, 'list.html', {'contacts': results, 'query': query})