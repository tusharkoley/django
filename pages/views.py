from django.shortcuts import render
from pages.namer import bob

def home(request):
	return render(request,"home.html", {}) 

def about( request):
	return render (request, "about.html",{"myName":bob})
# Create your views here.
