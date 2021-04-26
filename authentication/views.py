from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate, login, logout
from .models import DataStore
import re

def home(request):
        return render(request, "home.html")

def userView(request):
        return render(request, "userView.html")

def selectBus(request):
        source1 = request.POST.get('from')
        dest1 = request.POST.get('to')
        print(source1, dest1)
        
        store1 = DataStore.objects.get(source=source1,dest=dest1)
	
        messages.success(request, str(store1.busNo) )
        return render(request, "selectBus.html")

def pdetails(request):
	return render(request, "pdetails.html")

def thankyou(request):
	return render(request, "thankyou.html")


def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        EMAIL_REGIX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-copyZ0-9._-]+\.[a-zA-Z]+$')

        if not EMAIL_REGIX.match(request.POST["email"]):
            messages.error(request, " invalid email fromat! ex: test@test.com")
            return redirect('home')

        if User.objects.filter(username=request.POST["username"]).count() > 0:
            messages.error(request, " A user with this name already exixts!")
            return redirect('home')

        if User.objects.filter(email=request.POST["email"]).count() > 0:
            messages.error(request, "A user with this email already exixts!")

        if len(username)>10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')

        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " your account is successfully created")
        
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")


def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            
            ###########################################
            '''
            store1 = DataStore( source="mumbai", dest="pune", busNo="mh15-5634")
            store1.save()
            store1 = DataStore( source="mumbai", dest="nashik", busNo="mh15-3435")
            store1.save()
            '''
            #DataStore.objects.all().delete()
            ###########################################
            
            messages.success(request, "Successfully Logged In")
            return redirect("userView")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")
    else:
        return HttpResponse("404- Not found")
   
        #return HttpResponse("login")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')

