from django.shortcuts import render
from django.http import HttpResponse
from .forms import userForms


def main(request):
    return render(request,'main/main2.html')

def reg(request):
    form = userForms()
    data = {
        "form": form
    }
    return render(request,'main/registration.html', data)

def cm(request):
    return render(request,'main/coctails_make.html')

def search_of_ingrid(request):
    return render(request, "main/search_of_ingrid.html")

def prof(request):
    return render(request, "main/my_profile.html")

def log(request):
    return render(request, "main/login.html")