from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from models import Post,Category

def index(request):
    posts = Post.objects.all()
    categories = Category.objects.all()

    return render(request, 'blog/index.html', {'posts':posts, 'categories': categories})

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    categories = Category.objects.all()
    posts = Post.objects.all()
    prev = posts.filter(id__lt=pk).first()
    next = posts.filter(id__gt=pk).first()

    return render(request, 'blog/post.html', {'post': post, 'categories': categories, 'prev_post': prev, 'next_post': next})

def category(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    posts = cate.post_set.all()
    categories = Category.objects.all()

    return render(request, 'blog/index.html', {'posts': posts, 'categories': categories})

def about(request):
	return HttpResponse('Not yet...')
# Create your views here.
