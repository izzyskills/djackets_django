from django.shortcuts import render
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from . import serializers
from . import models

# Create your views here.


class LatestProductList(APIView):
    def get(self, request, format=None):
        products = models.Product.objects.all()[0:4]
        serializer = serializers.ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return models.Product.objects.filter(category__slug=category_slug).get(
                slug=product_slug
            )
        except models.Product.DoesNotExist:
            return Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = serializers.ProductSerializer(product)
        return Response(serializer.data)


class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return models.Category.objects.get(slug=category_slug)
        except models.Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = serializers.CategorySerializer(category)
        return Response(serializer.data)


@api_view(["POST"])
def search(request):
    query = request.data.get("query", "")

    if query:
        products = models.Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        serializer = serializers.ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})
