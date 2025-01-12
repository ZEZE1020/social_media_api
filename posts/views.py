from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-timestamp')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('-timestamp')



class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/post_create.html'
    fields = ['content', 'media']
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/post_update.html'
    fields = ['content', 'media']
    success_url = reverse_lazy('post-list')
