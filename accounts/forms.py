from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


# Register Form
class RegisterForm(UserCreationForm):

    first_name = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            "first_name",
            "username",
            "email",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.help_text = ""


# Edit User Form
class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            "first_name",
            "email",
        ]


# Edit Profile Form
class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = [
            "profile_image",
        ]