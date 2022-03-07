from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.CharField(max_length=50)  # 별도로 email 추가

    class Meta:
        model = User
        fields = ['username', 'email']