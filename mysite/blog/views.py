from django.shortcuts import render,get_object_or_404
from models import Post,Category

def index(request):
    posts = Post.objects.all()
    categories = Category.objects.all()

    return render(request, 'blog/indes.html', {'posts':posts, 'categories': categories})

def post(request,pk):
    post = get_object_or_404(Post, pk)
    categories = Category.objects.all()

    return render(request, 'blog/post.html', {'post': post, 'categories': categories})

def category(request,pk):
    posts = get_object_or_404(Post,pk)
    categories = Category.objects.all()

    return renser(request, 'blog/category.html', {'posts': posts, 'categories': categories})
# Create your views here.
