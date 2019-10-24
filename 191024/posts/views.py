from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        return render(request, 'posts/index.html')
    else:
        form = PostForm()
    context = {
        'form':form
    }
    return render(request, 'posts/form.html', context)

def detail(request, id):
    #posts로 쓰지마 post로 써! 하나만 불러오니까!
    post = Post.objects.get(id=id)
    context = {
        'post':post
    }
    return render(request, 'posts/detail.html', context)

def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('posts:index')