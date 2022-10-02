from django.urls import path
from accounts.views import (
    LoginView, logout_user, UserRegisterView, get_profile
    )

urlpatterns = [
    path('login/', LoginView.as_view(), name="sign_in"),
    path('registration/', UserRegisterView.as_view(), name="register"),
    path('logout/', logout_user, name="logout"),
    path('user_profile/', get_profile, name="user_profile")
]