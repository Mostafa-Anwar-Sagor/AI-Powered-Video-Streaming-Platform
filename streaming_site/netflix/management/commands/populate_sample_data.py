from django.core.management.base import BaseCommand
from netflix.models import Category, Video


class Command(BaseCommand):
    help = 'Populate the database with sample video content for StreamFlix'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting to populate sample data...'))
        
        # Create categories
        categories_data = [
            {'name': 'Trending', 'slug': 'trending', 'order': 1, 'description': 'Most popular content right now'},
            {'name': 'Popular', 'slug': 'popular', 'order': 2, 'description': 'All-time favorites'},
            {'name': 'New Releases', 'slug': 'new-releases', 'order': 3, 'description': 'Latest additions'},
            {'name': 'Documentaries', 'slug': 'documentaries', 'order': 4, 'description': 'Award-winning documentaries'},
            {'name': 'Technology', 'slug': 'technology', 'order': 5, 'description': 'Tech and innovation content'},
            {'name': 'Science', 'slug': 'science', 'order': 6, 'description': 'Scientific explorations'},
        ]
        
        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults=cat_data
            )
            categories[cat_data['slug']] = category
            if created:
                self.stdout.write(f"  Created category: {category.name}")
            else:
                self.stdout.write(f"  Category exists: {category.name}")
        
        # Sample videos
        videos_data = [
            {
                'title': 'AI Documentary: The Future',
                'slug': 'ai-documentary-future',
                'description': 'An in-depth exploration of artificial intelligence and its impact on society, technology, and the future of humanity. Featuring interviews with leading AI researchers and glimpses into cutting-edge AI labs.',
                'video_type': 'documentary',
                'thumbnail': 'https://picsum.photos/300/450?random=1',
                'hero_image': 'https://picsum.photos/1920/1080?random=hero1',
                'video_url': 'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4',
                'year': 2026,
                'duration_minutes': 135,
                'rating_percentage': 98,
                'age_rating': 'PG',
                'director': 'Sarah Chen',
                'cast': 'Dr. Andrew Ng, Fei-Fei Li, Yann LeCun',
                'language': 'English',
                'is_featured': True,
                'categories_slugs': ['trending', 'documentaries', 'technology']
            },
            {
                'title': 'Machine Learning Masterclass',
                'slug': 'ml-masterclass',
                'description': 'Learn the fundamentals of machine learning from world-renowned experts. This comprehensive series covers everything from basic concepts to advanced neural networks.',
                'video_type': 'series',
                'thumbnail': 'https://picsum.photos/300/450?random=2',
                'video_url': 'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4',
                'year': 2026,
                'duration_minutes': 320,
                'rating_percentage': 95,
                'age_rating': 'PG',
                'director': 'Michael Roberts',
                'cast': 'Multiple AI Experts',
                'language': 'English',
                'is_featured': False,
                'categories_slugs': ['trending', 'technology', 'popular']
            },
            {
                'title': 'Data Science Revolution',
                'slug': 'data-science-revolution',
                'description': 'How data science is transforming industries and changing the way we make decisions. Real-world case studies from healthcare, finance, and more.',
                'video_type': 'documentary',
                'thumbnail': 'https://picsum.photos/300/450?random=3',
                'video_url': 'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4',
                'year': 2025,
                'duration_minutes': 92,
                'rating_percentage': 92,
                'age_rating': 'PG',
                'director': 'Emily Watson',
                'cast': 'Industry Leaders, Data Scientists',
                'language': 'English',
                'is_featured': False,
                'categories_slugs': ['popular', 'technology', 'science']
            },
            {
                'title': 'Neural Networks Explained',
                'slug': 'neural-networks-explained',
                'description': 'A deep dive into the architecture and functioning of neural networks. Visual explanations make complex concepts accessible to everyone.',
                'video_type': 'short',
                'thumbnail': 'https://picsum.photos/300/450?random=4',
                'video_url': 'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4',
                'year': 2026,
                'duration_minutes': 45,
                'rating_percentage': 90,
                'age_rating': 'G',
                'director': 'Alex Kim',
                'cast': 'Visualized Narration',
                'language': 'English',
                'is_featured': False,
                'categories_slugs': ['new-releases', 'technology']
            },
            {
                'title': 'Quantum Computing: Next Frontier',
                'slug': 'quantum-computing-frontier',
                'description': 'Explore the revolutionary world of quantum computing and how it promises to solve problems that are impossible for classical computers.',
                'video_type': 'documentary',
                'thumbnail': 'https://picsum.photos/300/450?random=5',
                'video_url': 'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4',
                'year': 2025,
                'duration_minutes': 88,
                'rating_percentage': 87,
                'age_rating': 'PG',
                'director': 'Robert Chang',
                'cast': 'Quantum Physicists',
                'language': 'English',
                'is_featured': False,
                'categories_slugs': ['science', 'technology', 'popular']
            },
            {
                'title': 'The Code Breakers',
                'slug': 'code-breakers',
                'description': 'Stories of brilliant programmers and hackers who changed the world. From early computing pioneers to modern cybersecurity heroes.',
                'video_type': 'series',
                'thumbnail': 'https://picsum.photos/300/450?random=6',
                'video_url': 'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerJoyrides.mp4',
                'year': 2026,
                'duration_minutes': 240,
                'rating_percentage': 96,
                'age_rating': 'PG-13',
                'director': 'Jennifer Miller',
                'cast': 'Tech Industry Veterans',
                'language': 'English',
                'is_featured': False,
                'categories_slugs': ['trending', 'popular', 'documentaries']
            },
            {
                'title': 'Robotics in Action',
                'slug': 'robotics-action',
                'description': 'See how advanced robotics are being deployed in manufacturing, healthcare, and daily life. The future is automated.',
                'video_type': 'documentary',
                'thumbnail': 'https://picsum.photos/300/450?random=7',
                'video_url': 'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerMeltdowns.mp4',
                'year': 2026,
                'duration_minutes': 75,
                'rating_percentage': 93,
                'age_rating': 'G',
                'director': 'David Park',
                'cast': 'Robotics Engineers',
                'language': 'English',
                'is_featured': False,
                'categories_slugs': ['new-releases', 'technology', 'science']
            },
            {
                'title': 'Blockchain Decoded',
                'slug': 'blockchain-decoded',
                'description': 'Understanding blockchain technology beyond cryptocurrency. Applications in supply chain, voting systems, and digital identity.',
                'video_type': 'documentary',
                'thumbnail': 'https://picsum.photos/300/450?random=8',
                'video_url': 'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/Sintel.mp4',
                'year': 2025,
                'duration_minutes': 82,
                'rating_percentage': 85,
                'age_rating': 'PG',
                'director': 'Lisa Anderson',
                'cast': 'Blockchain Experts',
                'language': 'English',
                'is_featured': False,
                'categories_slugs': ['popular', 'technology']
            },
            {
                'title': 'Space Exploration 2026',
                'slug': 'space-exploration-2026',
                'description': 'The latest missions to Mars, the Moon, and beyond. Exclusive footage from space agencies and private space companies.',
                'video_type': 'documentary',
                'thumbnail': 'https://picsum.photos/300/450?random=9',
                'video_url': 'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4',
                'year': 2026,
                'duration_minutes': 105,
                'rating_percentage': 94,
                'age_rating': 'G',
                'director': 'Marcus Webb',
                'cast': 'Astronauts, Scientists',
                'language': 'English',
                'is_featured': False,
                'categories_slugs': ['new-releases', 'science', 'documentaries']
            },
            {
                'title': 'The Internet Revolution',
                'slug': 'internet-revolution',
                'description': 'How the internet transformed human civilization in just a few decades. Interviews with internet pioneers and tech visionaries.',
                'video_type': 'documentary',
                'thumbnail': 'https://picsum.photos/300/450?random=10',
                'video_url': 'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4',
                'year': 2025,
                'duration_minutes': 98,
                'rating_percentage': 91,
                'age_rating': 'PG',
                'director': 'Thomas Lee',
                'cast': 'Tech Pioneers',
                'language': 'English',
                'is_featured': False,
                'categories_slugs': ['popular', 'documentaries', 'technology']
            },
        ]
        
        # Create videos
        for video_data in videos_data:
            category_slugs = video_data.pop('categories_slugs')
            video, created = Video.objects.get_or_create(
                slug=video_data['slug'],
                defaults=video_data
            )
            
            # Add categories
            for slug in category_slugs:
                if slug in categories:
                    video.categories.add(categories[slug])
            
            if created:
                self.stdout.write(self.style.SUCCESS(f"  ✓ Created: {video.title}"))
            else:
                self.stdout.write(f"  ✓ Exists: {video.title}")
        
        self.stdout.write(self.style.SUCCESS('\n🎉 Sample data populated successfully!'))
        self.stdout.write(self.style.SUCCESS(f'Created {Category.objects.count()} categories and {Video.objects.count()} videos'))
        self.stdout.write(self.style.SUCCESS('\nYou can now:'))
        self.stdout.write('  1. Visit http://127.0.0.1:8000/ to see the StreamFlix homepage')
        self.stdout.write('  2. Visit http://127.0.0.1:8000/admin/ to manage content (admin/admin123)')
        self.stdout.write('  3. Add, edit, or delete videos and categories from the admin panel')
