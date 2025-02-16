from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Jeff P',
        'title': 'Python',
        'content': 'Beautiful is better than ugly',
        'date_posted' : 'Feb 16, 2025'
    },
{
        'author': 'Jeff P',
        'title': 'C#',
        'content': 'ugly is better than beautiful',
        'date_posted' : 'Feb 10, 2025'
    }
]

# Create your views here.

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})