from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


#def logout(request):
    #auth.logout(request)
   # return redirect("/") 


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        User=auth.authenticate(username=username,password=password)


        if User is not None:
            auth.login(request,user)
            return redirect("/")
        else :
            messages.info(request,'Invalid Credentials')
            return redirect('login')    
    else:
        return render(request,'login.html')    


# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1== password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'USERNAME TAKEN')
                return redirect('register')
            elif User.objects.filter(email=email).exists(): 
                    messages.info(request,'EMAIL TAKEN')
                    return redirect('register') 
            
            else:
                data=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name);
                data.save();
                return redirect('login')
            
        else:
            print('password is not matching.........')    
            return redirect('/')
    else:    
        return render(request,'register.html')




       