from django import forms
from django.forms import ModelForm
from .models import Post, Comment

class PostForm(forms.ModelForm):
    image=forms.ImageField(required=True)
    class Meta:
        model = Post
        exclude = ['author', 'slug'  ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']


class ContactForm(forms.Form):
    name=forms.CharField(max_length=100,required=True)
    email=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea,required=True)
   



