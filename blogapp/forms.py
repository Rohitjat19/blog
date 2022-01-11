from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder' ]= 'your username'
        self.fields['email'].widget.attrs['placeholder' ]= 'your email'
        self.fields['password1'].widget.attrs['placeholder' ]= 'password'
        self.fields['password2'].widget.attrs['placeholder' ]= 'confirm-password'
        
class LoginForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = ['username', 'password']
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder' ]= 'your username'
        self.fields['password'].widget.attrs['placeholder' ]= 'password'
        
