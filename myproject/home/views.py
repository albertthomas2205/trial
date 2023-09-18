from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def homee(request):
    if not request.user.is_authenticated:
        return redirect('signin')
        
    return render(request,"home/index.html")

def signup(request):
    if request.method =='POST':
        username = request.POST['username']
        fname= request.POST['fname']
        lname= request.POST['lname']
        email= request.POST['email']
        pass1= request.POST['pass1']
        pass2= request.POST['pass2']
        
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        
        
        myuser.save()
        
        messages.success(request,'Your account has been successfully registerd.')
        
        return redirect('signin')
        
         
    return render(request,'home/signup.html')

def signin(request):
    if request.user.is_authenticated:
        return redirect('homee')
    if request.method =="POST":
        username = request.POST['username']
        pass1 =  request.POST['pass1']
        
        user = authenticate(username= username,password = pass1)
        if user is not None:
            login(request,user)
            # fname = user.fname
            return render(request,'home/index.html')
        else:
            messages.error(request,'wrong username and passwords.')
            # return render(request,'home/erro1.html')
    return render(request,'home/signin.html')

def signout(request):
    logout(request)
    messages.success(request,'logged out successfully')
    return redirect('homee')
