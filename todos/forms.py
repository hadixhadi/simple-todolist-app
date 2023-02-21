from django import forms
from .models import Todos
class todoForm(forms.ModelForm):
    class Meta:
        model=Todos
        fields=['title','is_done']