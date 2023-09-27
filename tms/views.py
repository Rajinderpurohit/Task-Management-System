from django.shortcuts import render, redirect
from .models import CustomUser
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from . import forms, models
# Create your views here.


@login_required
def home(request):
    alltasks = models.Task.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'alltasks': alltasks,
    }
    return HttpResponse(template.render(context, request))


def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'Login Failed!'
        else:
            message = 'Form is not valid.'
    return render(request, 'login.html', context={'form': form, 'message': message})


def logout_user(request):
    if not request.user.is_authenticated:
        return redirect('index')
    logout(request)
    return redirect('index')


def sign_page(request):
    form = forms.SignForm()
    message = ''
    if request.method == 'POST':
        form = forms.SignForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password1']
            user = CustomUser.objects.create_user(username,email, password)
            user.save()
            message = f'{email}! You have been registered.'
    return render(request, 'sign.html', context={'form': form, 'message': message})

@login_required
def create_task(request):
    form = forms.TaskForm()
    message = ''
    if request.method == 'POST':
        request.POST._mutable = True
        request.POST['task_by'] = request.user.id
        form = forms.SaveTaskForm(request.POST)
        if form.is_valid():
            #title = form.cleaned_data['title']
            #desp = form.cleaned_data['description']
            #status = form.cleaned_data['status']
            #ddate = form.cleaned_data['ddate']
            #user = form.cleaned_data['assigned_to']
            #print(title, desp, status, ddate, user)
            form.save()
            return HttpResponse('Task Created Successfully !')
        else:
            print(form.errors)
            forms.TaskForm()
    allusers = models.CustomUser.objects.order_by().values_list('email').distinct()
    return render(request, 'task.html', {'form': form, 'allusers': allusers})

@login_required
def del_task(request):
    del_id = request.GET['taskid']
    if not del_id.isnumeric():
        return HttpResponse('Invalid Task Id')
    x = models.Task.objects.filter(id=int(del_id))
    x.delete()
    print(models.Task.objects.all())
    return HttpResponse('Task Deleted Successfully !')






