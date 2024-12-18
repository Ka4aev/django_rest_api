from .models import Author, Book
from rest_framework import serializers

# Create your models here.

class BookSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        source='author',
        write_only=True
    )
    author_name = serializers.CharField(source='author.full_name', read_only=True)
    book_link = serializers.HyperlinkedIdentityField(view_name='book-detail',lookup_field='pk')

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author_id', 'author_name', 'publisher_name','year_published',
            'genre', 'category',  'cover', 'book_file', 'book_link'
        ]

    def validate(self, attrs):
        title = attrs.get('title')
        author = attrs.get('author')
        year_published = attrs.get('year_published')
        publisher_name = attrs.get('publisher_name')

        if Book.objects.filter(
            title=title,
            author=author,
            year_published=year_published,
            publisher_name=publisher_name
        ).exists():
            raise serializers.ValidationError(
                "Книга с такими параметрами уже существует"
            )

        return attrs


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer( read_only=True, many=True)

    class Meta:
        model = Author
        fields = ['id', 'full_name', 'bio', 'books']






