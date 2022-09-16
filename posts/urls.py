from django.urls import path
from posts.views import index_page


urlpatterns = [
    path("", index_page)
]