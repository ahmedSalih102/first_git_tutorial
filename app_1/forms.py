from django import forms
from .models import Event,Partecipant,Sinup

class SinupForm(forms.ModelForm):
    class Meta:
        model=Sinup
        fields='__all__'
    