from django import forms
from . import models as md

class GenerativeForm(forms.ModelForm):
    class Meta:
        model = md.GenerativeModel
        fields = ('pdb', 'residue_name', 'iterations')
        widgets = {
            'pdb': forms.FileInput( attrs={'class': 'pdbclass'}),
            'residue_name': forms.TextInput(attrs={'class': 'residueclass'}),
            'iterations': forms.NumberInput(attrs={'class': 'iterationsclass'})

        }
        labels = {
            "pdb": "Ligand pdb:",
            "residue_name": "Ligand residue name:",
            "iterations": "Growing Iterations"
        }