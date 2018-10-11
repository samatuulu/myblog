from django.shortcuts import render
from .models import Post

from django.http import HttpResponse
#
# def hello(request):
#     return HttpResponse('<h2>Hello</h2>')
#


def post_list(request):
    posts = Post.objects.all()
    # posts = Post.objects.get(title="asd")
    return render(request, 'blog/index.html', context={'posts': posts})

