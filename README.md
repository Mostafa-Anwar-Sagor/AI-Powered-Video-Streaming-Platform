# 🎬 StreamFlix - Netflix-Style Video Streaming Platform

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.2-green.svg)
![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey.svg)
![License](https://img.shields.io/badge/License-BSD-blue.svg)
![Status](https://img.shields.io/badge/Status-Production-success.svg)

**Professional Netflix-Style Video Streaming Platform with AI-Powered Recommendations**

*Developed by Mostafa Anwar*

[Features](#-features) • [Screenshots](#-demo-screenshots) • [Installation](#-installation) • [Tech Stack](#-tech-stack) • [Author](#-author)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Demo Screenshots](#-demo-screenshots)
- [Installation](#-installation)
- [Usage](#-usage)
- [AI Recommendation Engine](#-ai-recommendation-engine)
- [Project Structure](#-project-structure)
- [Tech Stack](#-tech-stack)
- [Admin Panel](#-admin-panel-content-manager)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)
- [License](#-license)

---

## 🎯 Overview

**StreamFlix** is a fully-functional Netflix clone built with Django 5.2, featuring an authentic Netflix user interface, AI-powered content recommendations, and a professional content management system. The platform delivers a complete video streaming experience with advanced features including auto-rotating hero banners, dynamic content filtering, and intelligent video recommendations.

### 🔑 Key Highlights

- **🎨 Authentic Netflix UI** - Pixel-perfect Netflix interface with dark theme
- **🤖 AI Recommendations** - Intelligent content discovery based on viewing patterns
- **🎯 Dynamic Filtering** - Browse by TV Shows, Movies, New & Popular, My List
- **⚡ Auto-Rotating Hero** - Featured content carousel with smooth transitions
- **👤 User Authentication** - Secure login/register with session management
- **📊 Professional Admin** - Netflix-styled content management panel
- **📱 Responsive Design** - Optimized for desktop, tablet, and mobile
- **🔒 Role-Based Access** - Staff-only admin panel with user permissions

---

## ✨ Features

### 🎬 Public Interface

#### 🏠 Homepage
- **Hero Banner Rotation**: Auto-rotating featured videos every 6 seconds with fade transitions
- **Manual Controls**: Click indicator dots to jump to specific featured content
- **Category Rows**: Horizontally scrollable video rows organized by categories
- **AI Recommendations**: Dedicated section showing personalized video suggestions
- **Hover Effects**: Netflix-style card hover with scale animations

#### 🎥 Video Player
- **Full-Screen Playback**: Immersive video viewing experience
- **View Counter**: Automatic view count increment on playback
- **Smart Recommendations**: Shows related videos from same categories
- **Video Metadata**: Display title, description, cast, director, rating

#### 🔍 Browse Pages
- **TV Shows Filter**: View all series content (`?type=series`)
- **Movies Filter**: Browse movie catalog (`?type=movie`)
- **New & Popular**: Recently added content (last 30 days) (`?type=new`)
- **My List**: High-rated favorites (≥85% rating) (`?type=mylist`)
- **Dynamic Titles**: Page titles update based on current filter
- **Empty States**: Graceful handling when no content available

### 🔐 Authentication System

#### 📝 User Registration
- **Simple Signup**: Username, email, password with confirmation
- **Auto-Login**: Automatically logs in after successful registration
- **Validation**: Server-side validation for all input fields
- **Redirect**: Seamless redirect to homepage after registration

#### 🔑 Login System
- **Username-Based**: Login with username (not email)
- **Remember Me**: Optional persistent session
- **Error Handling**: Clear error messages for invalid credentials
- **Session Management**: Secure Django session handling

#### 👤 Profile Dropdown
- **Click Toggle**: Opens/closes on profile icon click
- **Menu Items**: Account, Transfer Profile, My List, Help Center, Sign out
- **Staff Access**: "Content Manager" link for admin users
- **Arrow Indicator**: Rotating arrow (▼ → ▲) shows dropdown state
- **Outside Click**: Automatically closes when clicking elsewhere

### 🎨 UI/UX Features

#### 🎭 Netflix-Style Design
- **Dark Theme**: #141414 background with #E50914 red accents
- **Fixed Navbar**: Solid background with backdrop blur effect
- **Smooth Transitions**: Fade animations for hero rotation (1s duration)
- **Hover States**: Interactive buttons with color/scale changes
- **Typography**: Helvetica Neue font matching Netflix branding

#### 📐 Layout & Spacing
- **Responsive Padding**: Proper clearance for fixed navbar (140px)
- **Grid System**: Category rows with flexible card layouts
- **Z-Index Management**: Proper layering (navbar: 1000, dropdown: 2000)
- **Scroll Behavior**: Smooth horizontal scrolling for video rows

---

## 📸 Demo Screenshots

> **📁 All screenshots are located in the [`screenshots/`](./screenshots/) directory**

### Homepage
- Hero banner with auto-rotating featured content
- Category-based video rows
- AI-powered recommendations section

### Browse Pages
- TV Shows, Movies, New & Popular, My List views
- Dynamic filtering and titles
- Responsive card layouts

### Video Player
- Full-screen playback interface
- Related content recommendations

### Admin Panel
- Dashboard with analytics
- Video/Category management
- Search and filtering tools

**[View all screenshots →](./screenshots/README.md)**

---

## 🚀 Installation

### Prerequisites
- **Python 3.11+** (tested with 3.11)
- **pip** (Python package manager)
- **Git** (for cloning repository)

### Step-by-Step Setup

```bash
# 1. Clone the repository
git clone https://github.com/Mostafa-Anwar-Sagor/Video-Streaming-Platform.git
cd Video-Streaming-Platform

# 2. Create and activate virtual environment
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install django pillow

# 4. Navigate to project directory
cd streaming_site

# 5. Run database migrations
python manage.py migrate

# 6. Load sample data (10 videos, 6 categories)
python manage.py populate_sample_data

# 7. Create admin user
python manage.py createsuperuser
# Username: admin
# Password: admin123

# 8. Mark videos as featured for hero rotation
python manage.py shell -c "from netflix.models import Video; videos = Video.objects.all()[:5]; [setattr(v, 'is_featured', True) for v in videos]; [v.save() for v in videos]; print('Featured videos set')"

# 9. Start development server
python manage.py runserver

# 10. Open browser
# Homepage: http://127.0.0.1:8000/
# Admin Panel: http://127.0.0.1:8000/content-manager/
# Django Admin: http://127.0.0.1:8000/admin/
```

### Default Credentials

| Type | Username | Password |
|------|----------|----------|
| **Admin/Staff** | admin | admin123 |
| **Regular User** | *(Create via registration)* | — |

---

## 📖 Usage

### Accessing the Platform

#### Public Routes
- **Homepage**: `http://127.0.0.1:8000/` - Hero banner, categories, AI recommendations
- **Browse All**: `http://127.0.0.1:8000/browse/` - All content
- **TV Shows**: `http://127.0.0.1:8000/browse/?type=series` - Series only
- **Movies**: `http://127.0.0.1:8000/browse/?type=movie` - Movies only
- **New & Popular**: `http://127.0.0.1:8000/browse/?type=new` - Recent content
- **My List**: `http://127.0.0.1:8000/browse/?type=mylist` - High-rated (≥85%)
- **Video Player**: `http://127.0.0.1:8000/watch/<id>/` - Video playback
- **Login**: `http://127.0.0.1:8000/login/` - User authentication
- **Register**: `http://127.0.0.1:8000/register/` - New user signup

#### Admin Routes (Staff Only)
- **Dashboard**: `http://127.0.0.1:8000/content-manager/` - Analytics overview
- **Video List**: `http://127.0.0.1:8000/content-manager/videos/` - Manage videos
- **Add Video**: `http://127.0.0.1:8000/content-manager/videos/add/` - Create video
- **Edit Video**: `http://127.0.0.1:8000/content-manager/videos/<id>/edit/` - Update video
- **Category List**: `http://127.0.0.1:8000/content-manager/categories/` - Manage categories
- **Django Admin**: `http://127.0.0.1:8000/admin/` - Full Django admin

### Managing Content

#### Adding Videos (Admin Panel)
1. Login as admin user (admin/admin123)
2. Click profile → "Content Manager"
3. Click "Videos" → "Add New Video"
4. Fill in:
   - **Title**: Video name
   - **Description**: Brief synopsis
   - **Thumbnail URL**: Image link
   - **Video URL**: Video file/embed link
   - **Categories**: Select one or more
   - **Type**: Movie, Series, Documentary, or Short Film
   - **Year**: Release year
   - **Rating**: 0-100 scale
   - **Duration**: Runtime in minutes
   - **Age Rating**: G, PG, PG-13, R, NC-17
   - **Cast**: Comma-separated actors
   - **Director**: Director name
   - **AI Score**: 0-100 recommendation weight
   - **AI Tags**: Comma-separated keywords
   - **Is Featured**: Check for hero rotation
   - **Is Active**: Publish status
5. Click "Save Video"

#### Managing Categories
1. Navigate to Content Manager → Categories
2. Click "Add New Category"
3. Enter:
   - **Name**: Category display name
   - **Slug**: URL-friendly identifier (auto-generated)
   - **Description**: Brief description
   - **Order**: Display order on homepage
   - **Is Active**: Visibility toggle
4. Click "Save Category"

---

## 🤖 AI Recommendation Engine

### Algorithm Overview

StreamFlix uses a hybrid scoring algorithm combining multiple factors:

```python
def get_ai_recommendations(video, limit=6):
    """
    Calculates AI recommendations based on 4 key factors
    """
    # Factor 1: Category Overlap (40% weight)
    shared_categories = calculate_shared_categories(video)
    category_score = min(shared_categories * 40, 40)
    
    # Factor 2: Rating Similarity (30% weight)
    rating_difference = abs(video.rating - candidate.rating)
    rating_score = max(30 - rating_difference, 0)
    
    # Factor 3: Popularity (20% weight)
    max_views = get_max_views()
    popularity_score = (candidate.view_count / max_views) * 20 if max_views > 0 else 0
    
    # Factor 4: Recency (10% weight)
    days_old = (datetime.now() - candidate.created_at).days
    recency_score = max(10 - (days_old / 365 * 10), 0)
    
    # Total Score
    total_score = category_score + rating_score + popularity_score + recency_score
    
    return sorted_videos[:limit]
```

### Scoring Breakdown

| Factor | Weight | Description |
|--------|--------|-------------|
| **Category Overlap** | 40% | Videos sharing more categories score higher |
| **Rating Similarity** | 30% | Videos with similar ratings (±10 points) |
| **Popularity** | 20% | View count normalization (0-100K views) |
| **Recency** | 10% | Newer content gets slight boost |

### Implementation

```python
# In netflix/models.py - Video model
def get_ai_recommendations(self, limit=6):
    videos = Video.objects.filter(
        is_active=True
    ).exclude(
        id=self.id
    ).prefetch_related('categories')
    
    scored_videos = []
    for video in videos:
        score = calculate_recommendation_score(self, video)
        scored_videos.append((video, score))
    
    # Sort by score descending and return top N
    scored_videos.sort(key=lambda x: x[1], reverse=True)
    return [video for video, score in scored_videos[:limit]]
```

### Displaying Recommendations

**Homepage AI Section**: Shows top 6 videos with rating ≥ 85%
```python
# In netflix/views.py
ai_recommendations = Video.objects.filter(
    is_active=True,
    rating__gte=85
).order_by('-ai_recommendation_score')[:6]
```

**Video Player Page**: Shows 6 related videos from same categories

---

## 📁 Project Structure

```
Video-Streaming-Platform/
├── streaming_site/              # Django project root
│   ├── manage.py                # Django management script
│   ├── db.sqlite3               # SQLite database
│   │
│   ├── streaming_site/          # Project settings
│   │   ├── settings/
│   │   │   ├── base.py          # Base settings
│   │   │   └── dev.py           # Development settings
│   │   ├── urls.py              # Root URL configuration
│   │   └── wsgi.py              # WSGI entry point
│   │
│   └── netflix/                 # Main application
│       ├── models.py            # Video & Category models (147 lines)
│       ├── views.py             # Public views (240 lines)
│       ├── admin_views.py       # Admin panel views (289 lines)
│       ├── urls.py              # URL routing (26 lines)
│       ├── admin.py             # Django admin config
│       │
│       ├── management/
│       │   └── commands/
│       │       └── populate_sample_data.py  # Sample data seeder
│       │
│       ├── templates/netflix/
│       │   ├── base.html        # Base template with navbar (501 lines)
│       │   ├── home.html        # Homepage with hero rotation (166 lines)
│       │   ├── browse.html      # Browse/filter pages (113 lines)
│       │   ├── player.html      # Video player
│       │   ├── login.html       # Login form (201 lines)
│       │   ├── register.html    # Registration form
│       │   │
│       │   └── admin/           # Admin panel templates
│       │       ├── base.html    # Admin base (348 lines)
│       │       ├── dashboard.html
│       │       ├── video_list.html
│       │       ├── video_edit.html
│       │       ├── category_list.html
│       │       └── category_edit.html
│       │
│       └── migrations/
│           ├── 0001_initial.py
│           └── 0002_video_ai_fields.py
│
├── venv/                        # Virtual environment
├── screenshots/                 # Demo screenshots
│   └── README.md                # Screenshot guide
├── docs/                        # Documentation
├── README.md                    # This file
└── test_setup.py                # Setup verification script
```

---

## 🛠 Tech Stack

### Backend
- **Framework**: Django 5.2.11
- **Language**: Python 3.11
- **Database**: SQLite 3 (development)
- **Authentication**: Django Sessions + User Model
- **ORM**: Django ORM with prefetch_related optimization

### Frontend
- **Template Engine**: Django Templates
- **CSS**: Custom CSS (Netflix theme)
- **JavaScript**: Vanilla JS (hero rotation, dropdown toggles)
- **Icons**: Unicode symbols (▼, ▲, 🤖)

### Database Schema

#### Video Model (19 fields)
```python
class Video(models.Model):
    title                    # CharField(200)
    description              # TextField
    thumbnail_url            # URLField
    video_url                # URLField
    categories               # ManyToManyField(Category)
    video_type               # CharField(choices)
    year                     # IntegerField(1900-2026)
    rating                   # IntegerField(0-100)
    duration                 # IntegerField (minutes)
    age_rating               # CharField
    view_count               # IntegerField (default=0)
    cast                     # TextField
    director                 # CharField
    is_featured              # BooleanField (hero rotation)
    is_active                # BooleanField (published)
    created_at               # DateTimeField (auto_now_add)
    updated_at               # DateTimeField (auto_now)
    ai_recommendation_score  # FloatField (0-100)
    ai_content_tags          # TextField (comma-separated)
```

#### Category Model (6 fields)
```python
class Category(models.Model):
    name          # CharField(100)
    slug          # SlugField (unique, auto-generated)
    description   # TextField
    order         # IntegerField (homepage display order)
    is_active     # BooleanField
    created_at    # DateTimeField
```

### URL Routing

| URL Pattern | View | Description |
|-------------|------|-------------|
| `/` | NetflixHomeView | Homepage with hero & categories |
| `/browse/` | BrowseView | Browse with optional `?type=` filter |
| `/watch/<id>/` | VideoPlayerView | Video player page |
| `/login/` | LoginView | User authentication |
| `/register/` | RegisterView | New user signup |
| `/logout/` | LogoutView | Session termination |
| `/content-manager/` | admin_dashboard | Admin dashboard (staff only) |
| `/content-manager/videos/` | admin_video_list | Video management |
| `/content-manager/videos/add/` | admin_video_edit | Add new video |
| `/content-manager/videos/<id>/edit/` | admin_video_edit | Edit video |
| `/content-manager/videos/<id>/delete/` | admin_video_delete | Delete video |
| `/content-manager/categories/` | admin_category_list | Category management |
| `/content-manager/categories/add/` | admin_category_edit | Add category |
| `/content-manager/categories/<id>/edit/` | admin_category_edit | Edit category |
| `/admin/` | Django Admin | Full Django admin interface |

---

## 🎛 Admin Panel (Content Manager)

### Dashboard Features
- **Total Videos**: Count of active videos
- **Total Categories**: Count of active categories
- **Total Views**: Sum of all video views
- **Total Users**: Registered user count
- **Recent Videos**: Last 5 added videos
- **Top Videos**: 5 most-viewed videos
- **Category Stats**: Video count per category (top 6)
- **New This Week**: Videos added in last 7 days

### Video Management
- **Search**: Search by title, description, director, cast
- **Filters**: Filter by category (slug) and type (movie/series)
- **Batch Actions**: View all, filter, search results
- **Edit Form**: 19 fields with validation
- **Thumbnails**: Display video thumbnails in list view
- **Status Indicators**: Active/Inactive badges

### Category Management
- **CRUD Operations**: Create, Read, Update, Delete categories
- **Video Count**: Shows number of videos per category
- **Order Management**: Set homepage display order
- **Slug Auto-Generation**: URL-friendly slugs
- **Bulk Toggle**: Activate/deactivate categories

### Security
- **@login_required**: All admin views require login
- **@user_passes_test**: Staff-only access (`is_staff=True`)
- **CSRF Protection**: Django CSRF tokens on all forms
- **Redirect on Unauthorized**: Non-staff users redirected to login

---

## 🔮 Future Enhancements

### Phase 1 - User Experience
- [ ] Comments and ratings system
- [ ] User playlists (custom lists)
- [ ] Watch history tracking
- [ ] Continue watching row
- [ ] Recently added section

### Phase 2 - Advanced Features
- [ ] PostgreSQL migration for production
- [ ] Redis caching for performance
- [ ] Elasticsearch for advanced search
- [ ] Video upload functionality
- [ ] Multiple video quality options

### Phase 3 - Social & Mobile
- [ ] Social sharing features
- [ ] User profiles with avatars
- [ ] Follow/friend system
- [ ] Mobile apps (React Native)
- [ ] Progressive Web App (PWA)

### Phase 4 - Monetization
- [ ] Subscription tiers
- [ ] Ad integration
- [ ] Pay-per-view content
- [ ] Content creator dashboard
- [ ] Revenue analytics

---

## 🐛 Known Issues & Troubleshooting

### Common Issues

**1. Server won't start**
```bash
# Make sure you're in the right directory
cd Video-Streaming-Platform/streaming_site

# Ensure virtual environment is activated
venv\Scripts\activate  # Windows

# Check if port 8000 is already in use
netstat -ano | findstr :8000  # Windows
lsof -i :8000  # macOS/Linux
```

**2. Database errors**
```bash
# Delete database and recreate
rm db.sqlite3
python manage.py migrate
python manage.py populate_sample_data
```

**3. Static files not loading**
```bash
# Collect static files
python manage.py collectstatic --no-input
```

**4. Admin login fails**
```bash
# Reset admin password
python manage.py shell -c "from django.contrib.auth.models import User; admin = User.objects.get(username='admin'); admin.set_password('admin123'); admin.save(); print('Password reset to admin123')"
```

---

## 📝 Development Notes

### Code Quality
- **Lines of Code**: ~2,500 total
- **Test Coverage**: In development
- **Documentation**: Inline comments + README
- **Code Style**: PEP 8 compliant

### Performance Optimizations
- **Database Queries**: `prefetch_related()` for categories
- **Template Caching**: Browser-side caching for static assets
- **Image Optimization**: URL-based images (no local storage overhead)
- **Lazy Loading**: Category rows load progressively

### Browser Compatibility
- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Edge 90+
- ✅ Safari 14+
- ⚠️ IE 11 (limited support)

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add AmazingFeature'`)
4. **Push** to branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Development Setup
```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/Video-Streaming-Platform.git

# Add upstream remote
git remote add upstream https://github.com/Mostafa-Anwar-Sagor/Video-Streaming-Platform.git

# Create branch
git checkout -b feature-name

# Make changes and commit
git add .
git commit -m "Description of changes"

# Push to your fork
git push origin feature-name
```

---

## 📄 License

**BSD 3-Clause License**

Copyright (c) 2026, Mostafa Anwar

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED.

---

## 👤 Author

<div align="center">

### Mostafa Anwar

**Software Engineer | Full-Stack Developer | AI Enthusiast**

[![Email](https://img.shields.io/badge/Email-sagorahmed1400%40gmail.com-red?style=flat-square&logo=gmail)](mailto:sagorahmed1400@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-%40Mostafa--Anwar--Sagor-181717?style=flat-square&logo=github)](https://github.com/Mostafa-Anwar-Sagor)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=flat-square&logo=linkedin)](https://linkedin.com)

</div>

### 📧 Contact

- **Email**: sagorahmed1400@gmail.com
- **GitHub**: [@Mostafa-Anwar-Sagor](https://github.com/Mostafa-Anwar-Sagor)
- **Portfolio**: *Coming soon*

### 🎯 Other Projects

- **Trading Platform** - AI-powered stock trading analysis
- **CRM SaaS Platform** - Customer relationship management system
- **Deepfake Detection** - Deep learning-based deepfake detection

---

## 🙏 Acknowledgments

- **Netflix** - UI/UX design inspiration
- **Django Community** - Excellent framework and documentation
- **Python Community** - Amazing ecosystem and libraries
- **Open Source Contributors** - For making development accessible

---

## 📊 Project Status

| Metric | Status |
|--------|--------|
| **Development** | ✅ Active |
| **Production Ready** | ✅ Yes |
| **Documentation** | ✅ Complete |
| **Test Coverage** | 🟡 In Progress |
| **Deployment** | 🟡 Local Only |

---

## 🎉 Project Statistics

- **Repository**: Video-Streaming-Platform
- **Created**: February 2026
- **Language**: Python (Django)
- **Stars**: ⭐ (Star this repo!)
- **Forks**: 🍴 (Fork and contribute!)
- **Issues**: 🐛 (Report bugs)

---

<div align="center">

### ⭐ Star this repo if you found it helpful!

**Built with ❤️ by Mostafa Anwar**

*Last Updated: February 7, 2026*

</div>


