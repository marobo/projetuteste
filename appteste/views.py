from django.shortcuts import render
from .models import Post


def index(request):
    my_dict = {"insert_me": "I am from views.py"}
    return render(request,'index.html',context=my_dict)


def post_list(request):
    posts = Post.objects.all().order_by('id')
    context = {
        'posts': posts,
    }
    return render(request,'appteste/post_list.html', context)