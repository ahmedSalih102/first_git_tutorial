from django.contrib import admin
from .models import Event,EventCatogry,Partecipant,Sinup
# Register your models here.
admin.site.register(Event)
admin.site.register(EventCatogry)
admin.site.register(Partecipant)
admin.site.register(Sinup)