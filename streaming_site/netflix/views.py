from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from .models import Video, Category
import json


class NetflixHomeView(TemplateView):
    template_name = 'netflix/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get multiple featured videos for hero rotation
        featured_videos = Video.objects.filter(is_featured=True, is_active=True)[:5]
        if featured_videos:
            context['featured_video'] = featured_videos[0]  # Primary for initial display
            context['featured_videos'] = list(featured_videos)  # All for rotation
            # JSON format for JavaScript
            context['featured_videos_json'] = json.dumps([
                {
                    'id': video.id,
                    'title': video.title,
                    'description': video.description,
                    'hero_image': video.hero_image,
                }
                for video in featured_videos
            ])
        else:
            context['featured_video'] = None
            context['featured_videos'] = []
            context['featured_videos_json'] = '[]'
        
        # Get videos organized by categories
        categories = Category.objects.filter(is_active=True).prefetch_related('videos')
        
        category_videos = {}
        for category in categories:
            videos = category.videos.filter(is_active=True)[:6]  # Limit to 6 videos per category
            if videos:
                # Convert to dict format for template compatibility
                category_videos[category.slug] = [
                    {
                        'id': video.id,
                        'title': video.title,
                        'thumbnail': video.thumbnail,
                        'rating': video.get_rating_display(),
                        'year': video.year,
                    }
                    for video in videos
                ]
        
        # Assign to context with common category names
        context['trending'] = category_videos.get('trending', [])
        context['popular'] = category_videos.get('popular', [])
        context['new_releases'] = category_videos.get('new-releases', [])
        context['documentaries'] = category_videos.get('documentaries', [])
        
        # If categories don't exist, show all videos in a single row
        if not category_videos:
            all_videos = Video.objects.filter(is_active=True)[:12]
            context['all_videos'] = [
                {
                    'id': video.id,
                    'title': video.title,
                    'thumbnail': video.thumbnail,
                    'rating': video.get_rating_display(),
                    'year': video.year,
                }
                for video in all_videos
            ]
        
        # AI-Powered Recommendations
        # Generate recommendations based on highest-rated videos and viewing patterns
        ai_recommended_videos = Video.objects.filter(
            is_active=True,
            rating_percentage__gte=85  # High-rated content
        ).order_by('-view_count', '-rating_percentage')[:6]
        
        context['ai_recommendations'] = [
            {
                'id': video.id,
                'title': video.title,
                'thumbnail': video.thumbnail,
                'rating': video.get_rating_display(),
                'year': video.year,
            }
            for video in ai_recommended_videos
        ]
        
        return context


class VideoPlayerView(TemplateView):
    template_name = 'netflix/player.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        video_id = self.kwargs.get('video_id')
        
        # Get the requested video
        video = get_object_or_404(Video, id=video_id, is_active=True)
        
        # Increment view count
        video.view_count += 1
        video.save(update_fields=['view_count'])
        
        context['video'] = {
            'id': video.id,
            'title': video.title,
            'description': video.description,
            'year': video.year,
            'rating': video.get_rating_display(),
            'duration': video.get_duration_display(),
            'video_url': video.video_url,
            'director': video.director,
            'cast': video.cast,
            'age_rating': video.age_rating,
        }
        
        # Get recommended videos from same categories
        video_categories = video.categories.all()
        recommended = Video.objects.filter(
            categories__in=video_categories,
            is_active=True
        ).exclude(id=video.id).distinct()[:3]
        
        context['recommended'] = [
            {
                'id': v.id,
                'title': v.title,
                'thumbnail': v.thumbnail
            }
            for v in recommended
        ]
        
        return context


class BrowseView(TemplateView):
    template_name = 'netflix/browse.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get filter parameters
        filter_type = self.request.GET.get('type', None)
        filter_category = self.request.GET.get('category', None)
        
        # Set page titles based on filter
        if filter_type == 'series':
            context['page_title'] = 'TV Shows'
            context['page_subtitle'] = 'Watch the latest series and TV shows'
        elif filter_type == 'movie':
            context['page_title'] = 'Movies'
            context['page_subtitle'] = 'Explore our collection of movies'
        elif filter_type == 'new':
            context['page_title'] = 'New & Popular'
            context['page_subtitle'] = 'Recently added content and trending now'
        elif filter_type == 'mylist':
            context['page_title'] = 'My List'
            context['page_subtitle'] = 'Your saved favorites'
        else:
            context['page_title'] = 'Browse All Content'
            context['page_subtitle'] = 'Discover thousands of shows and movies across all genres'
        
        # Get all active categories with their videos
        categories_data = []
        for category in Category.objects.filter(is_active=True).prefetch_related('videos'):
            videos = category.videos.filter(is_active=True)
            
            # Apply type filter
            if filter_type == 'series':
                videos = videos.filter(video_type='series')
            elif filter_type == 'movie':
                videos = videos.filter(video_type='movie')
            elif filter_type == 'documentary':
                videos = videos.filter(video_type='documentary')
            elif filter_type == 'new':
                # Get recently added videos or highly viewed content
                thirty_days_ago = timezone.now() - timedelta(days=30)
                recent_videos = videos.filter(created_at__gte=thirty_days_ago)
                if not recent_videos.exists():
                    # If no recent videos, show top rated and most viewed
                    videos = videos.order_by('-view_count', '-rating_percentage')
                else:
                    videos = recent_videos.order_by('-created_at')
            elif filter_type == 'mylist':
                # For My List, show highly rated content (user favorites not yet implemented)
                videos = videos.filter(rating_percentage__gte=85).order_by('-rating_percentage')
            
            if videos:
                categories_data.append({
                    'name': category.name,
                    'videos': [
                        {
                            'id': video.id,
                            'title': video.title,
                            'thumbnail': video.thumbnail,
                            'year': video.year,
                            'video_type': video.get_video_type_display(),
                            'age_rating': video.age_rating,
                        }
                        for video in videos[:12]  # Limit to 12 per category
                    ]
                })
        
        context['categories'] = categories_data
        
        return context


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('netflix:home')
        return render(request, 'netflix/login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('netflix:home')
        else:
            return render(request, 'netflix/login.html', {
                'error': 'Invalid username or password. Please try again.'
            })


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('netflix:home')
        return render(request, 'netflix/register.html')
    
    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        # Validation
        if password != password_confirm:
            return render(request, 'netflix/register.html', {
                'error': 'Passwords do not match.'
            })
        
        if User.objects.filter(username=username).exists():
            return render(request, 'netflix/register.html', {
                'error': 'Username already exists.'
            })
        
        if User.objects.filter(email=email).exists():
            return render(request, 'netflix/register.html', {
                'error': 'Email already registered.'
            })
        
        # Create user
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            # Auto login after registration
            login(request, user)
            return redirect('netflix:home')
        except Exception as e:
            return render(request, 'netflix/register.html', {
                'error': f'Registration failed: {str(e)}'
            })


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('netflix:login')
