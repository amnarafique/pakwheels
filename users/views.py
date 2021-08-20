from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.forms import ProfileRegistrationForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = ProfileRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = ProfileRegistrationForm()
    context = {
        'form': form
    }

    return render(request, 'users/register.html', context)


@login_required
def my_account(request):

    return render(request, 'home/my_account.html')


def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    form = ProfileUpdateForm(instance=request.user)
    context = {
        'form': form }

    return render(request, 'users/update_profile.html',context)


