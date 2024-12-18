
# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Author(models.Model):
    full_name = models.CharField(max_length=100, unique=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['full_name']


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publisher_name = models.CharField(max_length=100)
    year_published = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1000),
            MaxValueValidator(9999)
        ]
    )
    category = models.CharField(max_length=100)
    GENRE_CHOICES = [
        ('document', 'Document'),
        ('textbook', 'Textbook'),
        ('fantasy', 'Fantasy'),
        ('mystery', 'Mystery'),
        ('historical', 'Historical'),
    ]
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)

    book_file = models.FileField(upload_to='books/', blank=True, null=True)
    cover = models.ImageField(upload_to='book-covers/', blank=True, null=True)


    class Meta:
        unique_together = ('title', 'author', 'publisher_name', 'year_published', )

    def __str__(self):
        return f"{self.title} - {self.author.full_name}"

