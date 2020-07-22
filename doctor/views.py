from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def logindoctor(request):
    doc='I AM A DOCTOR'
    return HttpResponse(doc)


def signupdoctor(request):
    sign="DOCTOR SIGN UP"
    return HttpResponse(sign)




def home(request):
    re="redwas"
    return HttpResponse(re)
