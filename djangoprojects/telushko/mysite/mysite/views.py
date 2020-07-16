from django.http import HttpResponse
from django.shortcuts import render
from .models import Destination

def index (request):
    dest1=Destination()
    
    
    
    dests=Destination.objects.all()
    return render(request,'index.html',{'dests':dests})  
# Create your views here.

