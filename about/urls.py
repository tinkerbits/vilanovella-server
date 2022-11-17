from django.urls import path
from .views import AboutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', AboutView.as_view(), name="about"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)