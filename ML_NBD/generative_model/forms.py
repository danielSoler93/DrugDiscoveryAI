from django import forms
from . import models as md

class GenerativeForm(forms.ModelForm):
    class Meta:
        model = md.GenerativeModel
        fields = ('sdf', )