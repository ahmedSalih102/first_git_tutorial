
from django.urls import path
from .import views 

urlpatterns = [
    path('index',views.index,name='index' ),
    path('about',views.about,name='about' ),
    path('events',views.events,name='events' ),
    path('parts',views.parts,name='parts'),
    path('login',views.login,name='login'),
    path('sinup',views.sinup,name='sinup'),
]
