"""vilanovella_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap

from archive.models import Post

info_dict = {
    'queryset': Post.objects.all()
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
    path('archive/', include('archive.urls')),
    path('', include('home.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}}, name='django.contrib.sitemaps.views.sitemap'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
