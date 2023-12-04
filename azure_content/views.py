from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from .forms import *


class HomeView(ListView):
    context_object_name = 'project_list'
    model = Project
    template_name = "azure_content/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context

class AboutView(TemplateView):
    template_name = "azure_content/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About'
        return context


class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'description']
    template_name = "azure_content/create.html"
    success_url ="/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create'
        return context
    

class ProjectEditView(UpdateView):
    model = Project
    title = 'Edit'
    fields = ['name','description']
    template_name = "azure_content/create.html"
    success_url ="/"


class ProjectDeleteView(DeleteView):
    model = Project
    title = 'Delete'
    template_name = "azure_content/delete.html"
    fields = ['name']
    success_url ="/"

def Register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account was created')
                return redirect('/')
        context = {'form' : form}
        return render(request, 'azure_content/register.html', context)

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        login(request, user)
        # if user is not None:
        #     login(request, user)
        #     return redirect('/')
        # else:
        #     messages.info(request, 'Username or Password is incorrect!')

    context = {'title' : 'Login'}
    return render(request, 'azure_content/Login.html', context)


def Logout(request):
    logout(request)
    messages.info(request, 'You have logged out!')
    return redirect('login')
