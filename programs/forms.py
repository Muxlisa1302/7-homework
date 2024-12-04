from django import forms
from .models import ProgrammingLanguage

class ProgrammingLanguageForm(forms.ModelForm):
    class Meta:
        model = ProgrammingLanguage
        fields = ['title', 'description']
    method = 'POST'
