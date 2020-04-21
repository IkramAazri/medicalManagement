from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CreateUserForm


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Votre compte a été bien crée ! Veuillez se connecter!')

        return redirect("login")
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('register')
        else:
            messages.info(request, "Nom d'utilisateur ou mot de passe est incorrect")

    context = {}
    return render(request, 'accounts/login.html', context)
