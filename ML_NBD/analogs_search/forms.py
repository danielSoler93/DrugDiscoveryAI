from django import forms
from . import models as md


class AnalogsForm(forms.ModelForm):
    class Meta:
        model = md.AnalogsModel
        fields = ('query_sdf', 'email')
        labels = {
            "query_sdf": "Sdf of the molecule to query:"
        }