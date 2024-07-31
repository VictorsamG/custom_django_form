from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # return redirect('home')
            messages.success(request, ("Successfully logged in"))
            return redirect('/admin/')
        else:
            messages.error(request, ("There was an error loggin in, Try again"))
            return render(request, 'form.html')
            
    else:
        return render(request, 'form.html')