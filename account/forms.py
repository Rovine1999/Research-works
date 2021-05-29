from django import forms
from .models import *


class CreateUploadProfilePicForm(forms.ImageField):
    class Meta:
        model = UserProfile
        fields = ['profile_photo']
