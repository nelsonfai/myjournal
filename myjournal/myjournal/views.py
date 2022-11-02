from django.shortcuts import render


# Create your views here.
def home(request):
    pass
    return render (request,"main/home.html")
def setting(request):
    pass
    return render (request,"main/settings.html" ,{'pagetitle':'Settings'})