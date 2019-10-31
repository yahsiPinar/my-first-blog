from django import forms
from .models import Post,Commit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Commit
        fields = ('author','text')

class SignupForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

# post oluşturmak için bir form tasarladığımız için model post olmalı
# author burada zaten o an giriş yapmış olan admin olduğu için sadece 'title' ve 'text' alanlarını eklemek yeterli
