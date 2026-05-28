from django import forms
from .models import Conter

class ConterForm(forms.ModelForm):
    class Meta:
        model = Conter
        fields = ['ismi', 'familya', 'raqam', 'yoshi', 'stem_username', 'telegram_username']
        