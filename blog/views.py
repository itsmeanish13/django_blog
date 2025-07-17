from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

def index(request):
    name = 'Anish'
    posts =[
    {
        "title": "Introduction to Django",
        "author": "Alice Johnson",
        "category": "Web Development",
        "date": "2025-07-01"
    },
    {
        "title": "Understanding React Hooks",
        "author": "Bob Smith",
        "category": "Frontend",
        "date": "2025-06-20"
    },
    {
        "title": "Top 10 Python Tips",
        "author": "Carol Lee",
        "category": "Programming",
        "date": "2025-05-15"
    },
    {
        "title": "How AI is Changing the World",
        "author": "David Kumar",
        "category": "Artificial Intelligence",
        "date": "2025-07-10"
    },
    {
        "title": "Exploring REST APIs with Django",
        "author": "Ella Singh",
        "category": "Backend",
        "date": "2025-06-05"
    },
    {
        "title": "Mastering CSS Grid",
        "author": "Frank Turner",
        "category": "Design",
        "date": "2025-05-28"
    },
    {
        "title": "JavaScript ES6 Features",
        "author": "Grace Kim",
        "category": "JavaScript",
        "date": "2025-07-12"
    },
    {
        "title": "Building a Blog with Django",
        "author": "Harry Patel",
        "category": "Tutorial",
        "date": "2025-07-14"
    }
    ]
    context= {
        "name": name,
        "posts": posts
    }

    return render(request,'index.html',context)


# Create your views here.
