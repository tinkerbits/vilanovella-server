
from django.views.generic import TemplateView
from archive.views import PostListView


class HomeView(PostListView):
    template_name = 'home.html'

class RobotView(TemplateView):
    template_name = 'robots.txt'
    content_type = 'text/plain'