from unicodedata import category
from django.shortcuts import render
from rest_framework import generics

from .models import Book, Category, Product
from .serializers import CategorySerilaizer, BookSerializer, ProductSerializer


class ListCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerilaizer

class DetailCategory(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerilaizer

class ListBook(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DetailBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

