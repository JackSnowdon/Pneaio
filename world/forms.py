from django import forms
from .models import *

class NewCardForm(forms.ModelForm):
    
    class Meta:
        model = Card
        exclude = ['created_by']
