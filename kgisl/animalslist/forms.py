from django import forms
from .models import AnimalsList,SittingList,BreedList


class ViewSittingListForm(forms.Form):
    animal = forms.CharField(required=False)
    breed = forms.CharField(required=False, label='Breeds', widget=forms.Select(
        attrs={'name': 'breed', 'placeholder': 'Choose a Breed'}))
    date = forms.CharField(label="Date", initial='', required=False)

    def __init__(self, *args, **kwargs):
        super(ViewSittingListForm, self).__init__(*args, **kwargs)

        self.fields['animal'] = forms.ModelChoiceField(queryset=AnimalsList.objects.all(),
                                                              empty_label='Choose a Animal',
                                                              required=False)


    def clean(self):
        cleaned_data = super().clean()
        animal = cleaned_data.get("animal")
        breed = cleaned_data.get("breed")
        date = cleaned_data.get("date")

        if animal == '' or animal == None:
            msg = 'Please select a Animal Name'
            self.add_error('animal', msg)

        if breed == '' or breed == None:
            msg = 'Please select a Breed Name'
            self.add_error('breed', msg)

        if date == '':
            msg = 'Please select a Date'
            self.add_error('date', msg)