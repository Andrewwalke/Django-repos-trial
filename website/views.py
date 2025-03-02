from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def home(request):
    #check to see if user logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenicate
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been locked in")
            return redirect('home')
        else:
            messages.success(request,"There is something eerror when looging in")
            return redirect('home')
    else:
        return render(request,'home.html',{})




def logout_user(request):
    logout(request)
    messages.success(request,"You have been locked out")
    return redirect('home')



def register(request):
    return render(request,'register.html')
    