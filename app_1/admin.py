from django.contrib import admin
from .models import Event,EventCatogry,Partecipant
# Register your models here.
admin.site.register(Event)
admin.site.register(EventCatogry)
admin.site.register(Partecipant)