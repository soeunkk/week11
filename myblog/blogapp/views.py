from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from .forms import BlogModelForm

# Create your views here.
def home(request):
    return render(request, 'blogapp/home.html')

def blog(request):
    blogs = Blog.objects
    return render(request, 'blogapp/blog.html', {'blogs' : blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blogapp/detail.html', {'blog': blog_detail})

def new(request):
    return render(request, 'blogapp/new.html')

def modelformcreate(request):
    if request.method == 'POST':
        form = BlogModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = BlogModelForm()
    return render(request, 'blogapp/new.html', {'form': form})

def edit(request):
    return render(request, 'blogapp/edit.html')

def blogupdate(request, blog_id):
    post = get_object_or_404(Blog, pk = blog_id)
    if request.method == 'POST':
        form = BlogModelForm(request.POST, instance = post)
        if form.is_valid():
            form.save()
            return redirect('detail', blog_id = post.pk)
    else:
        form = BlogModelForm(instance = post)
        return render(request, 'blogapp/edit.html', {'form': form})

def blogdelete(request, blog_id):
    post = get_object_or_404(Blog, pk = blog_id)
    post.delete()
    return redirect('blog')