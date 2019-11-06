from django.shortcuts import render,get_object_or_404
from .models import Post,Commit
from django.utils import timezone
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts':posts})

def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request, 'blog/post_detail.html',{'post':post})

@login_required()
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm()
    return render(request,'blog/post_edit.html',{'form':form})

@login_required()
def post_edit(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        post = form.save(commit=False)
        post.author = request.user
        #post.published_date = timezone.now()
        post.save()
        return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request,'blog/post_edit.html',{'form':form})

@login_required()
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts':posts})

@login_required()
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_list')

@login_required()
def post_remove(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect('post_list')

@login_required()
def add_comment(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentForm()
    return render(request,'blog/add_comment.html', {'form': form})

@login_required()
def remove_comment(request,pk):
    comment = get_object_or_404(Commit,pk=pk)
    comment.delete()
    return redirect('post_detail',pk=comment.post.pk)

@login_required()
def approve_comment(request,pk):
    comment = get_object_or_404(Commit,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            userObject= form.cleaned_data
            username = userObject['username']
            password = userObject['password1']
            form.save()
            new_user = authenticate(username=username,password=password)
            login(request, new_user)
        return redirect('post_list')
    else:
        form = SignupForm()
    return render(request,'registration/signup.html',{'form':form})
