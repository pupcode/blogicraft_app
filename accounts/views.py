from django.shortcuts import get_object_or_404, redirect, render
from blog.models import Blog
from .forms import CreateUserForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile
from blog.decorators import unauthenticated_user
from blog.forms import CommentForm


# Create your views here.

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully- Kindly login')
            return redirect('login')

    context = {
        'form': form,
    }

    return render(request, 'accounts/authentication/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username or Password is Incorrect')

    context={

    }

    return render(request, 'accounts/authentication/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('index')


@login_required(login_url='login')
def my_profile(request):
    blog= Blog.objects.all()
    user = request.user
    user_profile = request.user.userprofile
    user_blogs = Blog.objects.filter(user=user)

 

    try:
        profile = user.userprofile
    except UserProfile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        if profile is None:
            profile = UserProfile.objects.create(user=user)
        profile_form = UserProfileForm(request.POST, request.FILES ,instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('my-profile')
    else:
        if profile is not None:
            profile_form = UserProfileForm(instance=profile)
        else:
            profile_form = UserProfileForm()    
    
    context = {
        'blog': blog,
        'profile_form': profile_form,
        'user_profile': user_profile,
        'user': user,
        'user_blogs': user_blogs,
    }

    return render(request, 'accounts/user/my-profile.html', context)

@login_required(login_url='login')
def update_profile(request):
    user = request.user
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=user.userprofile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('my-profile')
    else:
        profile_form = UserProfileForm(instance=user.userprofile)
    return render(request, 'my-profile', {'profile_form': profile_form})


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
    return render(request, 'accounts/user/blog-details.html', context)


@login_required(login_url='login')
def creators(request):
    profiles = UserProfile.objects.all()
    context={
        'profiles': profiles
    }
    return render(request, 'accounts/creators/creators.html', context)


@login_required(login_url='login')
def creator_details(request, username):
    # blog = Blog.objects.get(id=pk)
    profile = get_object_or_404(UserProfile, user__username=username)

    blogs = Blog.objects.filter(user=profile.user)

    context = {
        # 'blog': blog,
        'profile': profile, 
        'blogs': blogs
    }
    return render(request, 'accounts/creators/creator-details.html', context)