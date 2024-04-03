from django.urls import path
from .import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard' ),
    path('dashboard-more/', views.more, name='more' ),
    path('blog-details/', views.blog_details, name='blog-details' ),
    path('user-profile/', views.user_profile, name='user-page'),
    
    #search and filtering
    path('tag/<int:tag_id>/', views.tag_filter, name='tag_filter'),
    path('search/', views.blog_search, name='blog_search'),



    path('create-blog/', views.create_blog, name='create-blog'),
    path('edit-blog/<int:pk>/', views.edit_blog, name='edit-blog'),
    path('delete_blog/<int:pk>/', views.delete_blog, name='delete-blog'),
    path('success/', views.success_page, name='success-page'),

    path('dash-blog-details/<str:pk>/', views.blog_details, name='dash-blog-details' ),

    # path('delete_blog/<int:pk>/', views.delete_blog, name='delete_blog'),
    # path('view-blog/<str:pk>/', views.viewblog, name="view-blog"),
]