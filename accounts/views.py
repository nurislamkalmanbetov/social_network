from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse_lazy
from accounts.forms import LoginForm, UserRegisterForm

# Create your views here.
class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        username = data["username"]
        password = data["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect("index.html")
            return HttpResponse("Ваш аккаунт неактивен")
        return HttpResponse("Такого юзера не существует")


def register(request):
    return render(request, "register.html")


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("index.html")


class UserRegisterView(CreateView):
    template_name = "register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("index.html")


def get_profile(request):
    return render(request, "profile.html")
