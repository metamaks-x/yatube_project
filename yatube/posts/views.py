from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    template = 'posts/index.html'
    context = {
        'title': 'Это главная страница Yatube',
    }
    return render(request, template, context)


def group_posts(request):
    template = 'posts/group_list.html'
    context = {
        'title': 'Здесь будет информация о группах проекта Yatube',
    }
    return render(request, template, context)

# Create your views here.
