from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from.forms import SignUpForm,AddRecordForm
from .models import Record
# Create your views here.

def home(request):
    records = Record.objects.all()
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
        
        return render(request,'home.html',{'records':records})




def logout_user(request):
    logout(request)
    messages.success(request,"You have been locked out")
    return redirect('home')



def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and logging in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have been logged in succesfully")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})




def in_record(request,pk):
    if request.user.is_authenticated:
        #look up for record
        in_record = Record.objects.get(id=pk)
        return render(request,'record.html',{'in_record':in_record})
    else:
        messages.success(request,"You must login to view this page")
        return redirect('home')
    
    
    
def de_in_record(request,pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"Record deleted successfully")
        return redirect('home')
    else:
        messages.success(request,"You must be log in to do that")
        return redirect('home')
    


def add_in_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method =='POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request,"Record added")
                return redirect('home') 
       
        return render(request,'addrecord.html',{'form':form})
    
    else:
        messages.success(request,"You must bee logged in")
        return redirect('home')
    
    
def up_in_record(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance = current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"record has been updated")
            return redirect('home')
        
        return render(request,'update_record.html',{'form':form})
    
    else:
        messages.success(request,"You must be logged in")
        return redirect('home')