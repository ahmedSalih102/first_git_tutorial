from django.shortcuts import render
from django.http import HttpResponse
from .models import Event,EventCatogry,Partecipant
from app_1.forms import SinupForm
from django import forms
# Create your views here.

def index(request):
    return render(request , 'app_1/index.html',{'page_name':'this is index Page is wreten by Ahmed Salih'})

def about(request):
    return HttpResponse("About page")

def events(request):
    return render(request , 'app_1/events.html',{'events': Event.objects.all()})


def parts(request):
    return render(request,'app_1/parts.html',{'parts':Partecipant.objects.get(id=1)})

def login(request):
    return render(request,'app_1/login.html')

def sinup(request):
    data=SinupForm(request.POST)
    if data.is_valid():
        data.save()
    else:
        print( data.errors.as_data())
        ##data.errors
   
    return render(request,'app_1/sinup.html',{'sinup':SinupForm})

    # f_name=request.POST.get('f_name')
    #l_name=request.POST.get('l_name')
   # mobile=request.POST.get('mobile')
    #email=request.POST.get('email')
    #event=request.POST.get('event')
    #data=SinupForm(partecipant_first_name=f_name, partecipant_last_name= l_name,partecipant_email= email,partecipant_phone=mobile)
   #data.save()