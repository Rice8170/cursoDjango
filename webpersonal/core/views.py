from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    return render(request,"Core/home.html")

def about(request):
    return render(request,"Core/about.html")

def portafolio(request):
    return render(request,"Core/portafolio.html")

def contact(request):
    return render(request,"Core/contact.html")
