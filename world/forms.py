from django import forms
from .models import *

class NewCardForm(forms.ModelForm):
    
    class Meta:
        model = Card
        exclude = ['created_by']


class NewDeckForm(forms.ModelForm):

    class Meta:
        model = Deck
        fields = ['name']


class AddCardToDeck(forms.ModelForm):

    class Meta:
        model = CardInstance
        fields = ['card']


class NewBase(forms.ModelForm):

    class Meta:
        model = Base
        fields = ['name'] 
