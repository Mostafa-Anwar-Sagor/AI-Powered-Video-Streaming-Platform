from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum, Count, Q
from django.utils import timezone
from datetime import timedelta
from .models import Video, Category
from django.contrib.auth.models import User


def is_staff_user(user):
    return user.is_staff or user.is_superuser


@login_required
@user_passes_test(is_staff_user)
def admin_dashboard(request):
    """Netflix-style admin dashboard with analytics"""
    
    # Analytics
    total_videos = Video.objects.filter(is_active=True).count()
    total_categories = Category.objects.filter(is_active=True).count()
    total_views = Video.objects.aggregate(total=Sum('view_count'))['total'] or 0
    total_users = User.objects.count()
    
    # Recent videos
    recent_videos = Video.objects.filter(is_active=True).order_by('-created_at')[:5]
    
    # Top viewed videos
    top_videos = Video.objects.filter(is_active=True).order_by('-view_count')[:5]
    
    # Videos added this week
    week_ago = timezone.now() - timedelta(days=7)
    new_videos_count = Video.objects.filter(created_at__gte=week_ago).count()
    
    # Category distribution
    categories_with_count = Category.objects.annotate(
        video_count=Count('videos')
    ).order_by('-video_count')[:6]
    
    context = {
        'total_videos': total_videos,
        'total_categories': total_categories,
        'total_views': total_views,
        'total_users': total_users,
        'recent_videos': recent_videos,
        'top_videos': top_videos,
        'new_videos_count': new_videos_count,
        'categories_with_count': categories_with_count,
    }
    
    return render(request, 'netflix/admin/dashboard.html', context)


@login_required
@user_passes_test(is_staff_user)
def admin_video_list(request):
    """List all videos with search and filter"""
    
    query = request.GET.get('q', '')
    category_filter = request.GET.get('category', '')
    type_filter = request.GET.get('type', '')
    
    videos = Video.objects.all().order_by('-created_at')
    
    if query:
        videos = videos.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(director__icontains=query) |
            Q(cast__icontains=query)
        )
    
    if category_filter:
        videos = videos.filter(categories__slug=category_filter)
    
    if type_filter:
        videos = videos.filter(video_type=type_filter)
    
    all_categories = Category.objects.filter(is_active=True)
    
    context = {
        'videos': videos,
        'all_categories': all_categories,
        'query': query,
        'category_filter': category_filter,
        'type_filter': type_filter,
    }
    
    return render(request, 'netflix/admin/video_list.html', context)


@login_required
@user_passes_test(is_staff_user)
def admin_video_edit(request, video_id=None):
    """Create or edit a video"""
    
    video = None
    if video_id:
        video = get_object_or_404(Video, id=video_id)
    
    if request.method == 'POST':
        # Handle form submission
        title = request.POST.get('title')
        slug = request.POST.get('slug')
        description = request.POST.get('description')
        video_type = request.POST.get('video_type')
        thumbnail = request.POST.get('thumbnail')
        hero_image = request.POST.get('hero_image', '')
        video_url = request.POST.get('video_url')
        trailer_url = request.POST.get('trailer_url', '')
        year = request.POST.get('year')
        duration_minutes = request.POST.get('duration_minutes')
        rating_percentage = request.POST.get('rating_percentage')
        age_rating = request.POST.get('age_rating')
        director = request.POST.get('director', '')
        cast = request.POST.get('cast', '')
        language = request.POST.get('language', 'English')
        tags = request.POST.get('tags', '')
        is_featured = request.POST.get('is_featured') == 'true'
        is_active = request.POST.get('is_active') == 'true'
        category_ids = request.POST.getlist('categories')
        
        try:
            if video:
                # Update existing
                video.title = title
                video.slug = slug
                video.description = description
                video.video_type = video_type
                video.thumbnail = thumbnail
                video.hero_image = hero_image
                video.video_url = video_url
                video.trailer_url = trailer_url
                video.year = int(year)
                video.duration_minutes = int(duration_minutes)
                video.rating_percentage = int(rating_percentage)
                video.age_rating = age_rating
                video.director = director
                video.cast = cast
                video.language = language
                video.tags = tags
                video.is_featured = is_featured
                video.is_active = is_active
                video.save()
                
                video.categories.set(category_ids)
                messages.success(request, f'Video "{title}" updated successfully!')
            else:
                # Create new
                video = Video.objects.create(
                    title=title,
                    slug=slug,
                    description=description,
                    video_type=video_type,
                    thumbnail=thumbnail,
                    hero_image=hero_image,
                    video_url=video_url,
                    trailer_url=trailer_url,
                    year=int(year),
                    duration_minutes=int(duration_minutes),
                    rating_percentage=int(rating_percentage),
                    age_rating=age_rating,
                    director=director,
                    cast=cast,
                    language=language,
                    tags=tags,
                    is_featured=is_featured,
                    is_active=is_active
                )
                video.categories.set(category_ids)
                messages.success(request, f'Video "{title}" created successfully!')
            
            return redirect('netflix:admin_video_list')
        except Exception as e:
            messages.error(request, f'Error saving video: {str(e)}')
    
    all_categories = Category.objects.filter(is_active=True)
    
    context = {
        'video': video,
        'all_categories': all_categories,
        'video_types': Video.VIDEO_TYPE_CHOICES,
        'age_ratings': [choice[0] for choice in Video._meta.get_field('age_rating').choices],
    }
    
    return render(request, 'netflix/admin/video_edit.html', context)


@login_required
@user_passes_test(is_staff_user)
def admin_video_delete(request, video_id):
    """Delete a video"""
    video = get_object_or_404(Video, id=video_id)
    title = video.title
    video.delete()
    messages.success(request, f'Video "{title}" deleted successfully!')
    return redirect('netflix:admin_video_list')


@login_required
@user_passes_test(is_staff_user)
def admin_category_list(request):
    """List all categories"""
    categories = Category.objects.annotate(
        video_count=Count('videos')
    ).order_by('order', 'name')
    
    context = {'categories': categories}
    return render(request, 'netflix/admin/category_list.html', context)


@login_required
@user_passes_test(is_staff_user)
def admin_category_edit(request, category_id=None):
    """Create or edit a category"""
    
    category = None
    if category_id:
        category = get_object_or_404(Category, id=category_id)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        slug = request.POST.get('slug')
        description = request.POST.get('description', '')
        order = request.POST.get('order', 0)
        is_active = request.POST.get('is_active') == 'true'
        
        try:
            if category:
                category.name = name
                category.slug = slug
                category.description = description
                category.order = int(order)
                category.is_active = is_active
                category.save()
                messages.success(request, f'Category "{name}" updated successfully!')
            else:
                Category.objects.create(
                    name=name,
                    slug=slug,
                    description=description,
                    order=int(order),
                    is_active=is_active
                )
                messages.success(request, f'Category "{name}" created successfully!')
            
            return redirect('netflix:admin_category_list')
        except Exception as e:
            messages.error(request, f'Error saving category: {str(e)}')
    
    context = {'category': category}
    return render(request, 'netflix/admin/category_edit.html', context)


@login_required
@user_passes_test(is_staff_user)
def admin_category_delete(request, category_id):
    """Delete a category"""
    category = get_object_or_404(Category, id=category_id)
    name = category.name
    category.delete()
    messages.success(request, f'Category "{name}" deleted successfully!')
    return redirect('netflix:admin_category_list')
