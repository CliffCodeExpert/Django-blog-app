from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def about(request):
    return render(request,"about.html")

def sending_gmail(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
           name=form.cleaned_data['name']
           message = form.cleaned_data['message']
           email = form.cleaned_data['email']


           recipients = ['Youremail@example.com']
           html=render_to_string('message.html',{
            
            "name":name,
            "message":message,
            "email":email
           })
           send_mail(name,message,email, recipients,html_message=html)
           messages.info(request,f'Thanks {name}, Your Message Was Received,We will get back to you shortly')
           return redirect('sending_gmail')
    else:
        form=ContactForm()
    return render(request,"contact.html",{"form":form})

def new_post(request):
    if request.method == "POST":
            form = PostForm(request.POST, files=request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('home')
    else:
            form = PostForm()
    return render(request, "new_post.html", {'form': form} )
        
    
def post_details(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('post_details',slug=post.slug)
    else:
        form = CommentForm()
    return render(request, "add_comment.html", {'form': form, 'post': post})


def delete_post(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == "POST":
        post.delete()
        return redirect("home")
    return render(request, 'delete.html', {'post': post})









