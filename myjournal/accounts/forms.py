from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Profile

class SignUpForm (UserCreationForm):

    class Meta:
        model=User
        fields=('username','password1','password2','email', 'first_name','last_name')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form_control','placeholder': 'Username' }),
            'email': forms.EmailInput(attrs={'class': 'form_control','placeholder': 'Enter email here...' }),  
        }
    def __init__(self,*args,**kwargs):
            super(SignUpForm,self).__init__(*args,**kwargs)
            self.fields['password1'].widget.attrs['class']='form_control'
            self.fields['password1'].widget.attrs['placeholder']='Enter Password'
            self.fields['password2'].widget.attrs['class']='form_control'
            self.fields['password2'].widget.attrs['placeholder']='Re-enter Password'
            self.fields['first_name'].widget.attrs['class']='form_control'
            self.fields['first_name'].widget.attrs['placeholder']='First name'
            self.fields['last_name'].widget.attrs['class']='form_control'
            self.fields['last_name'].widget.attrs['placeholder']='Last name'

class LogInForm(AuthenticationForm):
    class Meta:
        model=AuthenticationForm
        fields=('username','password' )
    def __init__(self,*args,**kwargs):
        super(LogInForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form_control'
        self.fields['username'].widget.attrs['placeholder']='Username'
        self.fields['password'].widget.attrs['class']='form_control'
        self.fields['password'].widget.attrs['placeholder']='Enter Password'

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields=('about_me','date_of_birth', 'country','profilePic')
        widgets = {
            'about_me': forms.Textarea(attrs={'class': 'form_control','placeholder': 'Username','rows':5, 'cols':10 }),
              
        }
    def __init__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)
       #self.fields['profilePic'].widget.attrs['class']='form_control'
        self.fields['about_me'].widget.attrs['class']='form_control'
        self.fields['date_of_birth'].widget.attrs['class']='form_control'
        self.fields['country'].widget.attrs['class']='form_control'

class UserForm(ModelForm):
    class Meta:
        model = User

        fields=('username','email', 'first_name','last_name')
    def __init__(self,*args,**kwargs):
        super(UserForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form_control'
        self.fields['email'].widget.attrs['class']='form_control'
        self.fields['first_name'].widget.attrs['class']='form_control'
        self.fields['last_name'].widget.attrs['class']='form_control'




