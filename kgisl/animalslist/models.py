from django.db import models
from datetime import datetime
# Create your models here.

class AnimalsList(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.name

class BreedList(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    animalslist = models.ForeignKey(AnimalsList,on_delete=models.CASCADE, related_name='animals_list', blank=True, null=True)

    def __str__(self):
        return self.name

class SittingList(models.Model):
    animals_list = models.ForeignKey(AnimalsList,on_delete=models.CASCADE, blank=True, null=True)
    breeds_list = models.ForeignKey(BreedList, on_delete=models.CASCADE,
                                     blank=True, null=True)
    date = models.DateField(blank=True, default='', null=True)


