from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def home(request):
    #write = "testing 1 2"
    return render(request, 'home/home.html')
