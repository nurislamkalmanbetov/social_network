from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from posts.models import Post


# def index_page(request):
#     name = "Nuris"
#     products = ["Iphone", "Samsung", "RedMi", "Google"]
#     is_admin = True
#     context = {"name":name, "products":products, "is_admin":is_admin}
#     return render(request, 'index.html', context=context)

class IndexPage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context