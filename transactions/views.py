from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from . import models
from . import serializers
from django.core.serializers import serialize

class TransactionView(generics.ListCreateAPIView):
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer

    def get(self, request, pk = None):
        current_user = request.user
        transactions = models.Transaction.objects.filter(user__id = current_user.id)
        data = serialize('json', transactions)
        response = {
            'data': data
        }
        return Response(response)