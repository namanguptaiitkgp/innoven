from django import forms
from .models import Doc, Dialouge


class add_dialouge(forms.ModelForm):

    class Meta:
        model = Dialouge
        fields = '__all__'

class add_doc(forms.ModelForm):

    class Meta:
        model = Doc
        fields = '__all__'
