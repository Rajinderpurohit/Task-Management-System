from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Task


class SignForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(label='Email / Username',required=True)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'ddate', 'status', 'assigned_to')

class SaveTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'ddate', 'status', 'assigned_to', 'task_by')
