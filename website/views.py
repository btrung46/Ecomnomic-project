from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Product,Category,Customer,Order
from .form import SignUpForm
# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request,'home.html',{'products':products})
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate( username= username,password= password)
        if user is not None:
            login(request, user)
            messages.success(request,'you have been login!!!')
            return redirect('home')
        else:
            messages.success(request,'there are an error please try again!!')
            return redirect('login')
    else:
        return render(request,'login.html',{})
def logout_user(request):
    logout(request)
    messages.success(request,'you have been logout!!!')
    return redirect('login')
def about(request):
    return render(request,'about.html',{})
def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, 'you have been register and now you can view the website')
            return redirect('home')
    else:
        return render(request,'register.html', {'form':form})


def product_view(request, pk):
    if request.user.is_authenticated:
        product_detail = Product.objects.get(pk=pk)
        return render(request, 'product.html', {'product_detail':product_detail})
    else:
        messages.success(request, 'you must login to view this page')
        return redirect('home')
        
def category_view(request, foo):
    foo = foo.replace("-"," ")
    try:
        category = Category.objects.get(name= foo)
        products = Product.objects.filter(category = category)
        return render(request, 'category.html',{'category':category,'products':products})
    except:
        messages.success(request, 'category doesnt exsit ')