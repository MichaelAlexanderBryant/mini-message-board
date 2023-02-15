from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import Post

class PostListView(ListView):
    model = Post
    template_name = "post_list.html"

class PostCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["user", "message"]