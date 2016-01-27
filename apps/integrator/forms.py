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
    DOB  = forms.DateField(label = "Date of Birth")
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username','DOB')
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.username = self.cleaned_data["username"]
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            mydata = self.cleaned_data["DOB"]
            Wall_User.objects.create(DOB = mydata, user = user)
        return user

class messageForm(forms.ModelForm):
    class Meta:
        model = Wall_Message
        fields = ('message',)

class commentForm(forms.ModelForm):
    class Meta:
        model = Wall_Comment
        fields = ('comment',)
