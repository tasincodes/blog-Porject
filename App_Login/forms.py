from django import forms
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm,SetPasswordForm
from django.contrib.auth.models import User
from App_Login.models import *

class SignUpForm(UserCreationForm):
    email=forms.EmailField(label="email",required=True)
    class Meta:
        model=User
        fields = ('username','email','password1','password2')







class UserProfileChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password')

class ProfilePic(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields= ['profile_pic']

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']



