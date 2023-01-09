from django.shortcuts import get_object_or_404, render

from .models import Group, Post

LIMIT_RANGE = 10
LR = LIMIT_RANGE


def index(request):
    posts = Post.objects.order_by('-pub_date')[:LR]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:LR]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
