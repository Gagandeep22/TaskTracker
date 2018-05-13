from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from django.views import View
from .forms import UserRegistrationForm


# Create your views here.

class Register(View):
    form_class = UserRegistrationForm
    template_name = 'login/register.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # add to database
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/home')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
        else:
            form = UserRegistrationForm()
        return render(request, self.template_name, {'form': form})
