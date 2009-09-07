#!/usr/bin/env python

from django import forms
from models import Player

class RegisterPlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('name', 'email', 'estimate')
        
class RegisterResultForm(forms.Form):
    result = forms.IntegerField()
    
    def save(self, player=None):
        player.result = self.cleaned_data['result']
        player.score = player.estimate - player.result
        player.save()