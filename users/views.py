from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from users.forms import RegisterForm

# Create your views here.

def user_not_authenticated(request):
    if request.user.is_authenticated:
        return True
    return False


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        if user_not_authenticated(request):
            return redirect(reverse_lazy('channels:home'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        username = form.cleaned_data.get("username")
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        password = form.cleaned_data.get("password")
        # user object create
        user = User(username=username, first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        user.save()
        return redirect(reverse_lazy('users:login'))
    

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def dispatch(self, request, *args, **kwargs):
        if user_not_authenticated(request):
            return redirect(reverse_lazy('channels:home'))
        return super().dispatch(request, *args, **kwargs)


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')