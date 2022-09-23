from django.urls import path

from accounts.views import sign_in

urlpatterns = [
    path('login/', sign_in)
]