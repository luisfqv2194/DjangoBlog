from django.shortcuts import render
from django.http import HttpResponse
posts = [
    {
        'author': 'Luis',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 17, 2020'
    },
    {
        'author': 'Adriana',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 17, 2020'
    }
]


def home(request):
    return render(request, 'blog/home.html', {'posts': posts})


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
