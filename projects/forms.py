from django import forms
from .models import Doc, Dialouge, DSdate


class add_dialouge(forms.ModelForm):

    class Meta:
        model = Dialouge
        fields = '__all__'

class add_doc(forms.ModelForm):

    class Meta:
        model = Doc
        fields = '__all__'

class add_dsdate(forms.ModelForm):

    class Meta:
        model = DSdate
        fields = ['date', 'project', 'dealstage']

    date = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}),
        input_formats=('%d/%m/%Y',)
    )