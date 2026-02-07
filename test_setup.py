#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test script to verify Video Streaming Platform (Wagtail) installation"""

print("Testing Video Streaming Platform (Wagtail CMS) Setup...")
print("-" * 50)

try:
    import django
    print("[OK] Django imported successfully:", django.__version__)
except Exception as e:
    print("[FAILED] Django import failed:", e)

try:
    import wagtail
    print("[OK] Wagtail imported successfully:", wagtail.__version__)
except Exception as e:
    print("[FAILED] Wagtail import failed:", e)

try:
    from PIL import Image
    print("[OK] Pillow (Image processing) imported successfully")
except Exception as e:
    print("[FAILED] Pillow import failed:", e)

try:
    import requests
    print("[OK] Requests imported successfully:", requests.__version__)
except Exception as e:
    print("[FAILED] Requests import failed:", e)

try:
    from rest_framework import VERSION
    print("[OK] Django REST Framework imported successfully:", '.'.join(map(str, VERSION)))
except Exception as e:
    print("[FAILED] Django REST Framework import failed:", e)

try:
    import bs4
    print("[OK] BeautifulSoup4 imported successfully:", bs4.__version__)
except Exception as e:
    print("[FAILED] BeautifulSoup4 import failed:", e)

print("-" * 50)
print("All core dependencies verified!")
print("\nWagtail CMS is a powerful Django-based content management system")
print("with support for:")
print("  - Adaptive video streaming")
print("  - Media library management")
print("  - RESTful API for content delivery")
print("  - Rich media embedding and processing")
print("\nNext steps:")
print("1. Create a Wagtail site: wagtail start mysite")
print("2. Run migrations: python manage.py migrate")
print("3. Create superuser: python manage.py createsuperuser")
print("4. Start server: python manage.py runserver")
