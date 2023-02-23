from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Course, Topic, Student


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=['name']

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields=['course','title','url']
