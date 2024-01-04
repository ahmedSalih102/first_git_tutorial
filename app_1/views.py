from django.shortcuts import render
from django.http import HttpResponse
from .models import Event,EventCatogry,Partecipant
# Create your views here.

def index(request):
    return render(request , 'app_1/index.html',{'page_name':'this is index Page is wreten by Ahmed Salih'})

def about(request):
    return HttpResponse("About page")

def events(request):
    return render(request , 'app_1/events.html',{'events': Event.objects.all()})


def parts(request):
    return render(request,'app_1/parts.html',{'parts':Partecipant.objects.get(id=1)})