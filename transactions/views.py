from django.shortcuts import render
from rest_framework import generics

from . import models
from . import serializers

class TransactionView(generics.ListCreateAPIView):
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer
