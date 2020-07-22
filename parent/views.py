from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login

# Create your views here.



def loginparent(request):
    if request.method=='GET':
        return render(request, 'parent/loginparent.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is  None:
            return render(request, 'parent/loginparent.html', {'form': AuthenticationForm(), 'error':'username and password did not match'})
            #return render(request, 'todo/signup.html', {'form': UserCreationForm(), 'error':'password mismatch'})
        else:
            login(request, user)
            return redirect('homepage')
    #return render(request, 'todo/home.html')


def signupparent(request):
    if request.method=='GET':
        return render(request, 'parent/signupparent.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1']==request.POST['password2']:
            #check whether password1 matches password2
            try:
                user=User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('homepage')

            #check whether the username exists

            except IntegrityError:
                return render(request, 'parent/signupparent.html', {'form':UserCreationForm(), 'error':'Username already exists'})
        else:
            return render(request, 'parent/signupparent.html', {'form':UserCreationForm(), 'error':'Password Mismatch'})

def homepage(request):
    err="error"
    return HttpResponse(err)
