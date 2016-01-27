from django.shortcuts import render, redirect
from django.contrib.auth import forms,login,authenticate,logout
from django.views.generic import View
from django.contrib.auth.models import User
from .forms import UserFormRegistration,messageForm, commentForm
from django.contrib.auth.forms import UserCreationForm
from .models import Wall_Message, Wall_Comment, Wall_User, Wall
from django.apps import apps
Comment = apps.get_app_config('comments').models['comment']
Message = apps.get_app_config('posts').models['message']

class login_2(View):
    # this goes to our django.contrib.auth.forms and gets a prebuilt form
    form = forms.AuthenticationForm

    def get(self, request):
        context = {"login_form":self.form()}

        return render(request, 'integrator/login.html', context)

    def post(self,request):
        form = self.form(None, request.POST)
        context = {'form' : form}
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                #set session for user
                return redirect('/the_wall')
            else:
                return redirect('/')
        else:
            return redirect('/')

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
        return redirect('/')

def index(request):

    messages = Wall_Message.objects.filter(wall_id = request.user.wall.id)
    form = messageForm
    form2 = commentForm
    context = {"message_form":form(), "comment_form" : form2(), 'messages':messages}
    return render(request, "integrator/wall.html", context)

class create_comment(View):
    def post(self,request):
        message = Wall_Message.objects.get(id = request.POST['message'])
        comment = Wall_Comment.objects.create(message_id = message, comment_creator = request.user, comment = request.POST['comment'])


class create_message(View):
    def post(self,request):
        #allows for data checking if we set it as a form
        try:
            wall = Wall.objects.create(user = request.user)
        except:
            wall = Wall.objects.get(user = request.user)
        print wall.id
        Wall_Message.objects.create(wall = wall, message = request.POST['message'], message_creator = request.user)
        return redirect('/the_wall')
