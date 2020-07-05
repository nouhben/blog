from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
class UserRegisterFrom(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'class':'form-control p-2 mx-5'})
    )
    # To add classes to the rendred html but it is bad to do it here bcz it is 
    # somthing that should be done on the template not on the server ==> frontend
    # def __init__(self, *args, **kwargs):
    #     super(UserRegisterFrom,self).__init__(*args, *kwargs)
    #     for name in self.fields.keys():
    #         self.fields[name].widget.attrs.update({'class':'form-control p-2'})
    # class Meta:
    #     model = User
    #     fields = ['username','email','password1','password2']
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['image']


# Form rendring course 
# These below forms are not related to the project
class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')

class ColorfulContactForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'style': 'border-color: blue;',
                'placeholder': 'Write your name here',
                'class':'p-5 form-control'
            }
        )
    )
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'style': 'border-color: green;'})
    )
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs={'style': 'border-color: orange;'}),
        help_text='Write here your message!'
    )