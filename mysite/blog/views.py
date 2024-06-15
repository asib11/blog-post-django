from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'name': 'Asib',
        'occupation': 'student',
        'subject': 'CSE',
        'id': 18191103031,
        'section': 1,
        'intake': 40
    },
    {
        'name': 'Tanveer',
        'occupation': 'student',
        'subject': 'CSE',
        'id': 18191103037,
        'section': 1,
        'intake': 40
    }
]

# Create your views here.
def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')