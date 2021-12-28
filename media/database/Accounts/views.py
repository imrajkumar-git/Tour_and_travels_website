from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def logout(request):
        auth.logout(request)
        return render(request,'index.html')


def login (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user =auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

    return render(request,'login.html')




def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        print(username)
        first_name = request.POST['first_name']
        print(first_name)
        last_name = request.POST['last_name']
        print(last_name)
        email = request.POST['email']
        print(email)
        password = request.POST['password1']
        print(password)
        user=User.objects.create_user(username=username, password=password, email=email, first_name= first_name, last_name=last_name)
        print("user created")
        return redirect('login')
        user.save()
        
        
        

    return render(request, "register.html")

        