from archive.views import PostListView

class HomeView(PostListView):
    template_name = 'home.html'