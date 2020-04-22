from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect,get_object_or_404
from .forms import CreateUserForm
from django.template import loader
from django.http import HttpResponse

def index(request):
    context = {'segment': 'index'}
    return render(request, "index.html", context)


def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        context['segment'] = load_template

        template = loader.get_template('pages/' + load_template)
        return HttpResponse(template.render(context, request))

    except:

        template = loader.get_template('pages/error-404.html')
        return HttpResponse(template.render(context, request))


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
