from rest_framework import viewsets, permissions
from .models import CustomUser, Follow
from .serializers import UserSerializer, FollowSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserListView(ListView):
    model = CustomUser
    template_name = 'accounts/user_list.html'
    context_object_name = 'users'

class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'accounts/user_detail.html'
    context_object_name = 'user'

class UserCreateView(CreateView):
    model = CustomUser
    template_name = 'accounts/user_create.html'
    fields = ['username', 'email', 'password', 'bio', 'profile_picture']
    success_url = '/'
    
    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return redirect('home')

class UserUpdateView(UpdateView):
    model = CustomUser
    template_name = 'accounts/user_update.html'
    fields = ['username', 'email', 'bio', 'profile_picture']
    success_url = '/'

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    try:
        user_to_follow = CustomUser.objects.get(id=user_id)
        if Follow.objects.filter(follower=request.user, following=user_to_follow).exists():
            return Response({'detail': 'Already following this user.'}, status=status.HTTP_400_BAD_REQUEST)
        if request.user == user_to_follow:
            return Response({'detail': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
        Follow.objects.create(follower=request.user, following=user_to_follow)
        return Response({'detail': 'Followed successfully.'}, status=status.HTTP_200_OK)
    except CustomUser.DoesNotExist:
        return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    try:
        user_to_unfollow = CustomUser.objects.get(id=user_id)
        follow_instance = Follow.objects.filter(follower=request.user, following=user_to_unfollow)
        if follow_instance.exists():
            follow_instance.delete()
            return Response({'detail': 'Unfollowed successfully.'}, status=status.HTTP_200_OK)
        return Response({'detail': 'You are not following this user.'}, status=status.HTTP_400_BAD_REQUEST)
    except CustomUser.DoesNotExist:
        return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
