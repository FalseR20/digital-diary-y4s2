from rest_framework import generics

from . import serializers, models


class UserListAPIView(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = models.User.objects
    serializer_class = serializers.UserSerializer


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects
    serializer_class = serializers.UserSerializer
    lookup_field = 'username'
