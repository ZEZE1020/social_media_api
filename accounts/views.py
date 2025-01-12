from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Follow
from .serializers import FollowSerializer

User = get_user_model()
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    try:
        user_to_follow = User.objects.get(id=user_id)
        if Follow.objects.filter(follower=request.user, following=user_to_follow).exists():
            return Response({'detail': 'Already following this user.'}, status=status.HTTP_400_BAD_REQUEST)
        if request.user == user_to_follow:
            return Response({'detail': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
        Follow.objects.create(follower=request.user, following=user_to_follow)
        return Response({'detail': 'Followed successfully.'}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    try:
        user_to_unfollow = User.objects.get(id=user_id)
        follow_instance = Follow.objects.filter(follower=request.user, following=user_to_unfollow)
        if follow_instance.exists():
            follow_instance.delete()
            return Response({'detail': 'Unfollowed successfully.'}, status=status.HTTP_200_OK)
        return Response({'detail': 'You are not following this user.'}, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
