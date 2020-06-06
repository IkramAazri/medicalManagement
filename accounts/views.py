from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth

from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages
from django.views.generic import TemplateView, CreateView
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


# def TerrainUpdate(request, terrain_id):
#   terrain = get_object_or_404(Terrain, terrain_id=id)
#  form = TerrainForm(data=request.POST or None, instance=terrain)
#  if form.is_valid():
#    form.save()
#  messages.success(request, 'Your terrain is updated successfully!')
#  redirect('terrain')
# return render_to_response('accounts/terrain.html', {}, RequestContext(request))


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'accounts/profile-update.html'

    def post(self, request):
        post_data = request.POST or None
        file_data = request.FILES or None
        try:
            user_form = UserForm(post_data, instance=request.user)
            profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, 'Votre profil est bien modifié!')
                return HttpResponseRedirect(reverse_lazy('profile'))
        except Profile.DoesNotExist:
            user_form = UserForm(post_data, instance=request.user)
            profile_form = ProfileForm(request.POST, request.FILES)
            if user_form.is_valid() and profile_form.is_valid():
                new_user = user_form.save()
                profile = profile_form.save(commit=False)
                if profile.user_id is None:
                    profile.user_id = new_user.id
                profile_form.save()
                messages.success(request, 'Votre profil est bien modifié!')
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


def accueil(request):
    return render(request, "services.html")


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
            return redirect('accueil')
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
    messages.success(request, "Le compte a été desactivé !")
    return redirect('system_users')


@login_required()
def user_activate(request, user_id):
    user = User.objects.get(pk=user_id)
    user.is_active = True
    user.save()
    messages.success(request, "Le compte est activé!")
    return redirect('system_users')


def delete_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()
    messages.success(request, "Le compte est supprimé!")
    return redirect('system_users')


def logoutView(request):
    auth.logout(request)
    return render(request, 'accounts/logout.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.info(request, ('Votre mot de passe a été modifié!'))
            return redirect('change_password')
        password1 = request.POST.get('new_password1')
        password2 = request.POST.get('new_password2')
        if password1 != password2:
            messages.error(request, ("Mot de passe de confirmation ne correspond pas au nouveau mot de passe!"))
        else:
            messages.error(request, ("Mot de passe incorrect!"))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })
