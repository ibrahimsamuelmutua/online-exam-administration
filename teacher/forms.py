from django import forms
from django.contrib.auth.models import User
from . import models


class TeacherUserForm(forms.ModelForm):

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken. Please choose a different one.")
        return username

    class Meta:
        model = User
        fields = ['first_name', 'username', 'last_name', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = models.Teacher
        fields = ['address', 'mobile', 'profile_pic']
