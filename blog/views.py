from django.http import HttpResponseBadRequest
# from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .forms import BlogForm, CommentForm
from .models import Blog, Tag
from .decorators import unauthenticated_user
from django.db.models import Q
import random




from django.contrib.auth.decorators import login_required


# Create your views here.
# @unauthenticated_user
@login_required(login_url='login')
def dashboard(request):
    blog = Blog.objects.all()
    tags = Tag.objects.all()
    recent_blogs = Blog.objects.order_by('-date_created')[:4]
    discover_blogs = Blog.objects.order_by('date_created')[:6]

    # Shuffle the queryset randomly
    random_blogs = list(blog)
    random.shuffle(random_blogs)

    # Select the first 4 shuffled blogs
    featured_blogs = random_blogs[:4]

    context = {
        'blog': blog,
        'tags': tags,
        'recent_blogs': recent_blogs,
        "discover_blogs": discover_blogs,
        'featured_blogs': featured_blogs,


    }
    return render(request, 'blog/user/user-dashboard.html', context)

def blog_search(request):
    query = request.GET.get('query')
    if query:
        search_results = Blog.objects.filter(
            Q(title__icontains=query) |  # Search in blog titles
            Q(user__username__icontains=query)  # Search in usernames
        ).distinct()  # Ensure unique results
    else:
        search_results = []
    return render(request, 'blog/user/search_results.html', {'search_results': search_results, 'query': query})

@login_required(login_url='login')
def more(request):
    blog = Blog.objects.all()
    recent_blogs = Blog.objects.order_by('-date_created')
    context = {
        'blog': blog,
        'recent_blogs': recent_blogs,

    }
    return render(request, 'blog/user/more.html', context)

@login_required(login_url='login')
def tag_filter(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    filtered_blogs = Blog.objects.filter(tags=tag)
    context = {
        'tag': tag,
        'filtered_blogs': filtered_blogs,
    }
    return render(request, 'blog/user/tag_filter.html', context)

@login_required(login_url='login')
def blog_details(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    blog_creator = blog.user
    comments = blog.comments.all()  # Retrieve all comments associated with this blog post
    comment_count = comments.count()
    new_comment = None

    # If the request is a POST, process the comment form
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog = blog
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()  # Clear the form after successfully submitting a comment
            return redirect(request.path)

    else:
        comment_form = CommentForm()

    context = {
        'blog': blog,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'comment_count': comment_count,
        'blog_creator': blog_creator,
    }
    return render(request, 'blog/user/blog-details.html', context)


@login_required(login_url='login')
def user_profile(request):
    return render(request, 'blog/user/user-page.html')

@login_required(login_url='login')
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user  # Assign the current user to the user field
            blog.save()          
            return redirect('success-page')
    else:
        form = BlogForm()
    return render(request, 'accounts/user/crud/create-blog.html', {'form': form})

@login_required(login_url='login')
def success_page(request):
    return render(request, 'accounts/user/crud/success-page.html',)

@login_required(login_url='login')
def edit_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('success-page')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'accounts/user/crud/edit-blog.html', {'form': form})

@login_required(login_url='login')
def delete_blog(request, pk):
    if request.method == 'POST':
        blog = get_object_or_404(Blog, pk=pk)
        blog.delete()
        # Redirect back to the attendance page after deleting the record
        return redirect('success-page')
    else:
        # Handle GET request if needed (e.g., show an error page)
        return HttpResponseBadRequest("Invalid request")
    # return redirect('admin-dashboard')