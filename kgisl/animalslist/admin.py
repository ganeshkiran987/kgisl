from django.contrib import admin
from .models import AnimalsList,BreedList,SittingList

# Register your models here.
admin.site.register(AnimalsList)
admin.site.register(BreedList)
admin.site.register(SittingList)

