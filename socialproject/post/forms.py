from .models import post
from django import forms

class postcreate(forms.ModelForm):
    class Meta:
        model = post
        fields = ('title','image','caption')