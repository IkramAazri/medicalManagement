from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserForm, ProfileForm, TerrainForm, PatientForm
from django.contrib.auth.models import User
from .models import Profile, Terrain, Patient
from django.contrib import messages
from django.views.generic import TemplateView, CreateView


def patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('terrain')
    else:
        form = PatientForm()
    return render(request, "accounts/dossier.html", {"form": form})


def terrain(request):
    if request.method == "POST":
        form = TerrainForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
    else:
        form = TerrainForm()
    return render(request, "accounts/terrain.html", {"form": form})



def TerrainUpdate(request, terrain_id):
    terrain = get_object_or_404(Terrain, terrain_id=id)
    form = TerrainForm(data=request.POST or None, instance=terrain)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your terrain is updated successfully!')
        redirect('terrain')
    return render_to_response('accounts/terrain.html', {}, RequestContext(request))


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'accounts/profile-update.html'

    def post(self, request):
        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile = Profile(user=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.error(request, 'Your profile is updated successfully!')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
            user_form=user_form,
            profile_form=profile_form
        )

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


def index(request):
    context = {'segment': 'index'}
    return render(request, "home.html", context)


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


@login_required()
def registered_users(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'accounts/users.html', context)


@login_required()
def user_deactivate(request, user_id):
    user = User.objects.get(pk=user_id)
    user.is_active = False
    user.save()
    messages.success(request, "User account has been successfully deactivated!")
    return redirect('system_users')


@login_required()
def user_activate(request, user_id):
    user = User.objects.get(pk=user_id)
    user.is_active = True
    user.save()
    messages.success(request, "User account has been successfully activated!")
    return redirect('system_users')


def delete_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()
    messages.success(request, "The user is deleted")
    return redirect('system_users')
