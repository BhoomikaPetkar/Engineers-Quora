
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth


# Create your views here.
def quora(request):
    return render(request, 'quora.html')

def home(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        userName = request.POST['user name']
        password = request.POST['password']

        user = auth.authenticate(username= userName, password= password)

        if user is not None:
            auth.login(request,user)
            print("Logged in")
            return redirect('/accounts/home')

    else:
           return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        firstName = request.POST['first name']
        lastName = request.POST['last name']
        userName = request.POST['User name']
        Email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=userName, email=Email, password=password, first_name=firstName, last_name=lastName)
        print("New user created")

        return redirect('http://127.0.0.1:8000/accounts/login')

    else:
        return render(request, 'signup.html')


def about(request):
    return render(request, 'about.html')
