from django.conf import settings
from django.urls import path
from .import views
from django.conf.urls.static import static


urlpatterns = [
    #authentication
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),


    path('my-profile/', views.my_profile, name='my-profile' ),
    path('update-profile', views.update_profile, name='update-profile'),
    path('blog-details/<str:pk>/', views.blog_details, name='blog-details' ),

    path('creators/', views.creators, name='creators'),
    path('creator-profile/<str:username>', views.creator_details, name='creator-profile')
]