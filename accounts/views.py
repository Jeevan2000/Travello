from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth,User
# Create your views here.

def login(request):

    if request.method == "POST":
        user_name=request.POST['username']
        password1=request.POST['password']

        user=auth.authenticate(username=user_name,password=password1)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invlaid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')


def register(request):
    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        user_name=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        if password1==password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"User Name taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"E-mail ID taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=user_name,email=email,password=password1,first_name=first_name,last_name=last_name)
                user.save()
                print("user created")
                return redirect('login')
        else:
            messages.info(request,"Password - matching ")
            return redirect('register')

        return redirect("/")    
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def pune(request):
    return render(request,'pune.html')    

def mumbai(request):
    return render(request,'mumbai.html')       

def surat(request):
    return render(request,'surat.html')   

def bengalaru(request):
    return render(request,'bengalaru.html')       