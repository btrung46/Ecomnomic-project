from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html',{})
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['username']
        user = authenticate(request, username= username,password= password)
        if user is not None:
            pass
    return render(request, 'login.html',{})
def logout_user(request):
    pass 