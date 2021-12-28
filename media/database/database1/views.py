from django.shortcuts import render
from .models import Database


def database1(request):


    
    context = {
        'databases':Database.objects.all(),
        'count':Database.objects.all().count(),
        'Rajkumar': Database.objects.filter(vendor='Rajkumar Aryal').count(),
        'bashant':Database.objects.filter(vendor='Basanta Acharya').count(),
        'dewan':Database.objects.filter(vendor='Dewan Manandhar').count(),
        'sa':Database.objects.filter(vendor='Sachin Subedi').all(),
        'ba':Database.objects.filter(vendor='Basanta Acharya').all(),
        'de':Database.objects.filter(vendor='Dewan Manandhar').all(),

    }
 
    return render(request,'index.html',context)
