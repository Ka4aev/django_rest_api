
# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets, filters
from .permissions import IsAdminUser
# Импорты моделей и сериализаторов
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления авторами.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления книгами.
    Только администраторы могут изменять данные, остальные имеют доступ только для чтения.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'genre', 'author__full_name']
