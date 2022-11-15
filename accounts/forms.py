from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# 회원가입 폼
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 
            'username',
            'password1',
            'password2',
            'profile_image',
            'address',
        ]

        labels = {"profile_image":"프로필 이미지", "address": "주소"}

# 회원 프로필 수정 폼
class CustomUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(
        label=(""),
        help_text=''
        )
    class Meta:
        model = get_user_model()
        fields = [
            'profile_image',
            'address',
        ]
        labels = {"profile_image":"프로필 이미지 변경","address": "주소 변경"}