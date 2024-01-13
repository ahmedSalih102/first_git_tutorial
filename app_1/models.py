from django.db import models
from django.utils import timezone

# Create your models here.


class EventCatogry(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    max_number_of_participant = models.IntegerField()
    event_catogry = models.ForeignKey(EventCatogry, on_delete=models.CASCADE)
    event_location = models.CharField(max_length=255)
    event_discription = models.TextField()
    #is_active=models.BooleanField(default=True)
    event_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name= 'Event'
        ordering =['name']


class Partecipant(models.Model):
    partecipant_first_name = models.TextField(max_length=20)
    partecipant_last_name = models.TextField(max_length=20)
    partecipant_pict = models.ImageField(upload_to='photos/%y/%m/%d')
    partecipant_email = models.EmailField()
    partecipant_phone = models.IntegerField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.partecipant_first_name


class Sinup (models.Model):
    partecipant_first_name = models.CharField(max_length=20)
    partecipant_last_name = models.CharField(max_length=20)
    partecipant_email = models.EmailField()
    partecipant_phone = models.CharField(max_length=20)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    partecipant_pict = models.ImageField(upload_to='photos/%y/%m/%d')
    def __str__(self) -> str:
        return self.partecipant_first_name