from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'topic']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'slug': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'form-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['topic'].empty_label = 'Тема не выбрана'

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 100:
            raise ValidationError('Заголовок длиннее 100 символов')

        return title
