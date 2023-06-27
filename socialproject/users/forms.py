from django import forms 
from django.contrib.auth.models import User
from .models import profile


class usereditform(forms.ModelForm):
        class Meta:
                model = User
                fields = ('first_name','last_name','email')


class profileditform(forms.ModelForm):
        class Meta:
                model = profile
                fields = ('photo',)



class loginform(forms.Form):
         username = forms.CharField()
         password = forms.CharField(widget=forms.PasswordInput)
         
class userregistrationform(forms.ModelForm):
        
        password = forms.CharField(label='password',widget=forms.PasswordInput)
        password2  = forms.CharField(label='password2',widget=forms.PasswordInput)
        
        class Meta:
                model = User
                fields = {'username','email','first_name'}

        def check_password(self):
                if self.cleaned_data['password'] != self.cleaned_data['password2'] :
                        raise forms.ValidationError('Password do not match')
                
                return self.cleaned_data['password2']
        

        