from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from . import models
from . import serializers
from users.serializers import UserSerializer

class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

    def put(self, request, pk, format=None):
        user = models.CustomUser.objects.get(pk = pk)
        request.data['username'] = user.username
        request.data['password'] = user.password
        serializer = UserSerializer(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
