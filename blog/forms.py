from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text')


# post oluşturmak için bir form tasarladığımız için model post olmalı
# author burada zaten o an giriş yapmış olan admin olduğu için sadece 'title' ve 'text' alanlarını eklemek yeterli
