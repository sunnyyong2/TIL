from django.shortcuts import render, redirect, get_object_or_404
from .models import Poster
from .forms import PosterForm
from IPython import embed
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    boards = Poster.objects.all()
    context = {
        'boards': boards,
    }
    return render(request, 'board/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        posterform = PosterForm(request.POST)
        if posterform.is_valid():
            posterform.save()
            # poster = posterform.save(commit=False)
            # poster.user = request.user
            # poster.save()
            return redirect('board:index')
        else:
            form = PosterForm()  # 폼을 자동으로 불러온다
            context = {
                'form': form
            }
            return render(request, 'board/form.html', context)

    else:
        form = PosterForm()  # 폼을 자동으로 불러온다
        context = {
            'form': form
        }
        return render(request, 'board/form.html', context)


def detail(request, id):
    # DB(해당 모델)에서 같은 id를 가진 게시글 가져오기
    poster = Poster.objects.get(id=id)
    context = {
        'poster': poster,
    }
    return render(request, 'board/detail.html', context)


def delete(request, id):
    poster = Poster.objects.get(id=id)
    poster.delete()
    return redirect('board:index')


def update(request, id):
    poster = Poster.objects.get(id=id)
    if request.method == 'POST':
        posterform = PosterForm(request.POST, instance=poster)
        if posterform.is_valid():
            posterform.save()
            return redirect('board:detail', id)
    else:
        form = PosterForm(instance=poster)
        context = {
            'form': form,
        }
        return render(request, 'board/form.html', context)
 # 기존의 게시글 내용이 적힌 폼 보여주기
 # form.html의 action을 빈칸으로 두는 이유
 # redirect 변수 할당
 # 모델폼 매개변수 1. request.POST 2. instance


@login_required
def like(request, id):
    user = request.user
    post = get_object_or_404(Poster, id=id)
    if user in post.like_users.all():
        post.like_users.remove(user)
    else:
        post.like_users.add(user)
    return redirect('board:index')
