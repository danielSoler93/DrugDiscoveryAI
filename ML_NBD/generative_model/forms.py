from django import forms

class GenerativeForm(forms.Form):
    complex = forms.CharField(label="Sdf ligand")