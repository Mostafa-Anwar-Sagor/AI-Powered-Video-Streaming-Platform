from django.urls import path
from . import views, admin_views

app_name = 'netflix'

urlpatterns = [
    # Public Pages
    path('', views.NetflixHomeView.as_view(), name='home'),
    path('watch/<int:video_id>/', views.VideoPlayerView.as_view(), name='player'),
    path('browse/', views.BrowseView.as_view(), name='browse'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    
    # Netflix-Style Admin Panel
    path('content-manager/', admin_views.admin_dashboard, name='admin_dashboard'),
    path('content-manager/videos/', admin_views.admin_video_list, name='admin_video_list'),
    path('content-manager/videos/add/', admin_views.admin_video_edit, name='admin_video_add'),
    path('content-manager/videos/<int:video_id>/edit/', admin_views.admin_video_edit, name='admin_video_edit'),
    path('content-manager/videos/<int:video_id>/delete/', admin_views.admin_video_delete, name='admin_video_delete'),
    path('content-manager/categories/', admin_views.admin_category_list, name='admin_category_list'),
    path('content-manager/categories/add/', admin_views.admin_category_edit, name='admin_category_add'),
    path('content-manager/categories/<int:category_id>/edit/', admin_views.admin_category_edit, name='admin_category_edit'),
    path('content-manager/categories/<int:category_id>/delete/', admin_views.admin_category_delete, name='admin_category_delete'),
]
