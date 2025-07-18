from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post, Category
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')



def index(request):
    post_detail = Post.objects.all()
    return render(request, 'index.html', {'post_detail': post_detail})



# Create your views here.
def post_detail(request):
    post = get_object_or_404(Post)
    return render(request, 'post_detail.html', {'post': post})

def bio(request,id):
    post = get_object_or_404(Post,id=id)
    return render(request, 'bio.html', {'post': post})
