from django import forms
from .models import EducationalContent

class EducationalContentForm(forms.ModelForm):
    class Meta:
        model = EducationalContent
        fields = ['title', 'url']
