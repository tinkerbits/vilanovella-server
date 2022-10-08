from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse
from .models import Post
from .forms import CommentForm

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newest_post_first'] = Post.objects.all().order_by('-created')
        return context



class BlogDetailView(FormMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        kwargs = self.kwargs
        context = super().get_context_data(**kwargs)
        thispost = Post.objects.get(id=kwargs.get('pk'))
        thispostscomments = thispost.comments.all()
        context['comments'] = thispostscomments
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        postid = self.kwargs['pk']
        form.instance.related_post = Post.objects.get(id=postid)
        form.save()
        return super(BlogDetailView, self).form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.id})
    

