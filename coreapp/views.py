from django.shortcuts import render
from blog.models import Blog
# from django.contrib.auth.decorators import login_required
from blog.decorators import unauthenticated_user

# Create your views here.

@unauthenticated_user
def index(request):

    blog = Blog.objects.all()
    recent_blogs = Blog.objects.order_by('-date_created')[:6]


    context = {
        'blog': blog,
        'recent_blogs': recent_blogs,
    }

    return render(request, 'core/homepage.html', context)

def blog(request):

    blog = Blog.objects.all()

    context = {
        'blog': blog,
    }

    return render(request, 'core/blog.html', context)

def custom_404_view(request, exception):
    return render(request, 'core/404.html', status=404)
