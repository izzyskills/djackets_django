from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from . import models

# Create your views here.


class LatestProductList(APIView):
    def get(self, request, format=None):
        products = models.Product.objects.all()[0:4]
        serializer = serializers.ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
