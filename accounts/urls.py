from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic import TemplateView
from .views import ProfileUpdateView, ProfileView

urlpatterns = [
    path('home', views.index, name='home'),
    path('accueil',views.accueil,name='accueil'),
    re_path(r'^.*\.html', views.pages, name='pages'),
    path('register/', views.registerPage, name="register"),
    path('', views.loginPage, name="login"),
    path('logout/', views.logoutView, name="logout"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_complete"),


    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('users/', views.registered_users, name='system_users'),
    path('activate/user/<int:user_id>', views.user_activate, name='activate_user'),
    path('deactivate/user/<int:user_id>', views.user_deactivate, name='deactivate_user'),
    path('delete/user/<int:user_id>', views.delete_profile, name='delete_user'),


]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)