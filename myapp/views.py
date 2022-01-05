from __future__ import unicode_literals
from Travels_place_table.models import TravelsPlacePath
from User_api.models import CustomUser
from django.shortcuts import render,redirect
from myapp.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from myapp.models import *
import sqlite3

def signin(request):
    data=Customersignup(request.GET)
    if data.is_valid():
        username = data.cleaned_data['uname']
        emailid = data.cleaned_data['email']
        password = data.cleaned_data['psw']
        repassword = data.cleaned_data['pswrepeat']
        e=webpage(name=username,Email=emailid,password=password,repassword=repassword)
        
        e.save()
     
    return render(request,'register.html',{})
def contact1(request):
    data=contactus(request.GET)
    if data.is_valid():
        fullname = data.cleaned_data['fullname']
        Email = data.cleaned_data['Email']
        msg = data.cleaned_data['msg']

        e=contact(fullname=fullname,Email=Email,msg=msg)
       
        e.save()
    return render(request, 'contact.html', {})
def loginforms(request):
    if request.method=="GET":
        data = Loginform(request.GET)
    try:
        if data.is_valid():
            u = data.cleaned_data['uname']
            p = data.cleaned_data['psw']
            user = webpage.objects.get(name=u, password=p)

            if u == user.name and p == user.password:
                request.session["name"] = user.name
                request.session["password"] = user.password
           

            return redirect(request, "/prot/loggedin.html/", {})

    except:
        return render(request, "loggedin.html", {})

def logout(request):
    try:
      del request.session["name"]


    except:
        pass
    # return HttpResponse("<strong>You are logged out.</strong>")
    return redirect('/myapp/login/')
    # return render(request,'travelagency/index.html',{})

def database(request):
   
 
    return render(request,'home.html')

def database1(request):
    context = {
        'databases':TravelsPlacePath.objects.all(),
     
    }
 
    return render(request,'Travelsplace_Database.html',context)
def database3(request):
    context = {
        'database':CustomUser.objects.all(),
    }
    return render(request,'user.html',context)