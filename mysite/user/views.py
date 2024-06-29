from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth.decorators import  login_required # type: ignore
from django.contrib import messages # type: ignore
from .froms import UserRegistrationFrom

from django.contrib.auth import logout
from django.views import View

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created for {username}. Now you can log in')
            return redirect('login')
    else:
        form = UserRegistrationFrom()
    return render(request, 'user/register.html', {'form':form})

class CustomLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, f'Logout Successfully')
        # return redirect('login')
        return render(request, 'user/logout.html')

@login_required
def profile(request):
    return render(request, 'user/profile.html')