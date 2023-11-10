from django.shortcuts import render
from django.shortcuts import redirect
from .models import Post
from .forms import PostForm


def index(request):
    my_dict = {"insert_me": "I am from views.py"}
    return render(request,'index.html',context=my_dict)

def post_create(request):
    form = PostForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect ('post_list')
    context = {
        "form":form
    }
    return render(request, 'appteste/post_create.html', context)


def post_list(request):
    posts = Post.objects.all().order_by('id')
    context = {
        'posts': posts,
    }
    return render(request,'appteste/post_list.html', context)