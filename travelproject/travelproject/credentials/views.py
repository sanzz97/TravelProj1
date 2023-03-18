from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth


# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None: #if user is authenticated/registered already
            auth.login(request,user)
            return redirect('/')
        else: #if user is not registered
            messages.info(request,'invalid credentials')
            return redirect('login')

    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():#to check whether the username already exists in db
                messages.info(request,'Username already registered')
                return redirect('register') #if already registered then redirect to register page (register-name)
            elif User.objects.filter(email=email).exists():#to check whether the email already exists in db
                messages.info(request,'email id already registered')
                return redirect('register')
            else: # only if all the above is not satisfied then create the user
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save()
                # print('user created')
                return redirect('login') #if registered sucessfully, then goes to login

        else:
            messages.info(request,'password not matched')
            return redirect('register') #if password is not matched also be in register page
            # print('password not matching')
        return  redirect('/') #if password is matched redirect to home page
    return render(request,'register.html')
