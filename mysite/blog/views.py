from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Asib Ahmed',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2024'
    },
    {
        'author': 'Tanveer Tayeb',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2024'
    }
]

# Create your views here.
def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')