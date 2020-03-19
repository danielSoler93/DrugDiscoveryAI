from django import forms
from . import models as md

class GenerativeForm(forms.ModelForm):
    class Meta:
        model = md.GenerativeModel
        fields = ('pdb', 'residue_name', 'iterations')