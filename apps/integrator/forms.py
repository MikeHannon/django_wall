from django import forms
from django.contrib.auth.models import User
from django.forms.fields import DateField
# from Apps.get_app_config('comments') import Comment
# from Apps.get_app_config('posts') import Message
from django.contrib.auth.forms import UserCreationForm
from .models import Wall_User, Wall_Comment, Wall_Message
#ModelForm???

class UserFormRegistration(UserCreationForm):
    # first, last name email and username from here,
    # password and confirm from UserCreationFrom
    # DOB from Wall_User
    first_name = forms.CharField(label = "First Name")
    last_name = forms.CharField(label = "Last Name")
    email = forms.EmailField(label = "Email")
    username = forms.CharField(label = "Username")
    class Meta:
        model = Wall_User
        fields = ('first_name', 'last_name', 'email', 'DOB',)
    def save(self, commit = True):
        Wall_User.user = super(UserFormRegistration, self).save(commit=False)

        Wall_User.user.first_name = self.cleaned_data["first_name"]
        Wall_User.user.last_name = self.cleaned_data["last_name"]
        Wall_User.user.email = Wall_User.self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password1"])
        if commit:
            Wall_User.user.save();
            return user;



class messageForm(forms.ModelForm):
    class Meta:
        model = Wall_Message
        fields = ('message',)

class commentForm(forms.ModelForm):
    class Meta:
        model = Wall_Comment
        fields = ('comment',)
