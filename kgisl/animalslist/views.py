from django.shortcuts import render,redirect
from .forms import ViewSittingListForm
from .models import SittingList,AnimalsList,BreedList


#Displaying Animals List
def viewanimals(request):
    form = ViewSittingListForm()
    sittinglist = SittingList.objects.all()
    args = {'form': form, 'sittinglist': sittinglist}
    return render(request, 'animals.html', args)

#Loading Breeds
def loadbreeds(request):
    animal = request.GET.get('animal')
    breeds = BreedList.objects.filter(animalslist=animal)
    return render(request,'breeds_list.html',{'breeds':breeds})

#Delete data
def deletesittinglist(request):
    value = request.GET.get('value')
    SittingList.objects.filter(id=value).delete()
    return redirect('/animals')

#Creating Data
def createsittinglist(request):
    animal = request.GET.get('animal')
    breed = request.GET.get('breed')
    date = request.GET.get('date')
    animal_data = AnimalsList.objects.get(id=animal)
    breed_data = BreedList.objects.get(name=breed,animalslist=animal_data)
    SittingList.objects.create(animals_list=animal_data,breeds_list=breed_data,date=date)
    sittinglist = SittingList.objects.all()
    return render(request, 'animals.html', {'sittinglist': sittinglist})
