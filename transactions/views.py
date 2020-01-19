from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from . import models
from . import serializers
from django.core.serializers import serialize

class TransactionView(generics.ListCreateAPIView):
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer