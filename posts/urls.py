# posts/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet
from . import views

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/create/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/update/<int:pk>/', views.PostUpdateView.as_view(), name='post-update'),
]
