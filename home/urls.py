from django.urls import path
from .views import HomeView, RobotView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('robots.txt', RobotView.as_view(), name='robots.txt'),
    path('', HomeView.as_view(), name="home"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)