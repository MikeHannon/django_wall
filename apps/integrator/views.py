from django.shortcuts import render
from django.contrib.auth import forms,login,authenticate,logout
from django.views.generic import View
from .forms import UserFormRegistration,messageForm, commentForm
from django.contrib.auth.forms import UserCreationForm

class login(View):
    # this goes to our django.contrib.auth.forms and gets a prebuilt form
    form = forms.AuthenticationForm

    def get(self, request):
        context = {"login_form":self.form()}

        return render(request, 'integrator/login.html', context)

    def post(self,request):
        print request.POST
        print self.form(request.POST).is_valid()
        context = {"login_form": self.form()}
        return render(request, 'integrator/login.html',context)

class register(View):
    # this goes to our django.contrib.auth.forms and gets a prebuilt form
    form = UserFormRegistration

    def get(self, request):
        context = {"registration_form":self.form()}
        return render(request, 'integrator/registration.html', context)

    def post(self,request):
        registration = self.form(request.POST)
        if registration.is_valid():
            user = registration.save()
            print ("*")*50
            print user
            print ("*")*50
            #request.session['user'] = user

        else:
            context = {"registration_form":self.form()}
            return render(request, 'integrator/registration.html', context)
        return render(request, 'integrator/wall.html')
