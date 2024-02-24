from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class UserCreateForm(UserCreationForm):
    phone_number = forms.CharField(max_length=100, required=True)
    personal_account = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = "username", "password1", "password2", "email", "first_name", "last_name"

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(UserCreateForm, self).save(commit=True)
        user_profile = UserProfile(user=user,
                                   phone_number=self.cleaned_data['phone_number'],
                                   personal_account=self.cleaned_data['personal_account'],
                                   )
        user_profile.save()
        return user
