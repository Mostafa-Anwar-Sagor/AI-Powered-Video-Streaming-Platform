from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    """Categories for organizing videos (Trending, Popular, Documentaries, etc.)"""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0, help_text="Display order on homepage (lower numbers first)")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name


class Video(models.Model):
    """Main video/movie/show model"""
    
    VIDEO_TYPE_CHOICES = [
        ('movie', 'Movie'),
        ('series', 'TV Series'),
        ('documentary', 'Documentary'),
        ('short', 'Short Film'),
    ]
    
    # Basic Information
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    video_type = models.CharField(max_length=20, choices=VIDEO_TYPE_CHOICES, default='movie')
    
    # Media Files
    thumbnail = models.URLField(help_text="Thumbnail image URL (300x450px recommended)")
    hero_image = models.URLField(blank=True, help_text="Hero banner image URL (1920x1080px)")
    video_url = models.URLField(help_text="Video file URL or streaming link")
    trailer_url = models.URLField(blank=True, help_text="Trailer video URL")
    
    # Metadata
    year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2100)])
    duration_minutes = models.IntegerField(help_text="Duration in minutes")
    rating_percentage = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Rating as percentage (0-100)"
    )
    age_rating = models.CharField(
        max_length=10, 
        choices=[
            ('G', 'G - General'),
            ('PG', 'PG - Parental Guidance'),
            ('PG-13', 'PG-13'),
            ('R', 'R - Restricted'),
            ('NC-17', 'NC-17'),
        ],
        default='PG'
    )
    
    # Categorization
    categories = models.ManyToManyField(Category, related_name='videos')
    tags = models.CharField(max_length=200, blank=True, help_text="Comma-separated tags")
    
    # Additional Info
    director = models.CharField(max_length=100, blank=True)
    cast = models.CharField(max_length=500, blank=True, help_text="Comma-separated cast names")
    language = models.CharField(max_length=50, default='English')
    
    # Status
    is_featured = models.BooleanField(default=False, help_text="Show in hero banner")
    is_active = models.BooleanField(default=True)
    view_count = models.IntegerField(default=0)
    
    # AI Features
    ai_recommendation_score = models.FloatField(
        default=0.0,
        help_text="AI-calculated recommendation score (0-100)"
    )
    ai_content_tags = models.TextField(
        blank=True,
        help_text="AI-generated content tags for improved search"
    )
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} ({self.year})"
    
    def get_duration_display(self):
        """Convert minutes to hours and minutes"""
        hours = self.duration_minutes // 60
        minutes = self.duration_minutes % 60
        if hours > 0:
            return f"{hours}h {minutes}m"
        return f"{minutes}m"
    
    def get_rating_display(self):
        """Format rating as percentage"""
        return f"{self.rating_percentage}%"
    
    def get_ai_recommendations(self, limit=6):
        """AI-powered content recommendations based on categories, tags, and rating"""
        # Get similar videos from same categories
        same_categories = Video.objects.filter(
            categories__in=self.categories.all(),
            is_active=True
        ).exclude(id=self.id).distinct()
        
        # Calculate similarity scores based on:
        # 1. Shared categories (weight: 40%)
        # 2. Similar ratings (weight: 30%)
        # 3. View count popularity (weight: 20%)
        # 4. Recent releases (weight: 10%)
        
        recommendations = []
        for video in same_categories:
            # Calculate category overlap
            shared_cats = set(self.categories.values_list('id', flat=True)) & \
                         set(video.categories.values_list('id', flat=True))
            category_score = (len(shared_cats) / max(self.categories.count(), 1)) * 40
            
            # Rating similarity (closer ratings = higher score)
            rating_diff = abs(self.rating_percentage - video.rating_percentage)
            rating_score = max(0, (100 - rating_diff) / 100 * 30)
            
            # Popularity score
            popularity_score = min(video.view_count / 1000, 1) * 20
            
            # Recency score (newer videos get boost)
            days_old = (self.created_at - video.created_at).days
            recency_score = max(0, (365 - abs(days_old)) / 365) * 10
            
            total_score = category_score + rating_score + popularity_score + recency_score
            recommendations.append((video, total_score))
        
        # Sort by score and return top results
        recommendations.sort(key=lambda x: x[1], reverse=True)
        return [video for video, score in recommendations[:limit]]
