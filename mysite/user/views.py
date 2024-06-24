from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.contrib import messages # type: ignore
from .froms import UserRegistrationFrom

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!!!')
            return redirect('blog-home')
    else:
        form = UserRegistrationFrom()
    return render(request, 'user/register.html', {'form':form})