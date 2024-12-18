from django.db import models

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
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    year_published = models.PositiveIntegerField(
        validators=[
            MinValueValidator(500),
            MaxValueValidator(10000)
        ]
    )
    genre = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    publisher_name = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='book-covers/', blank=True, null=True)
    book_file = models.FileField(upload_to='books/', blank=True, null=True)

    class Meta:
        unique_together = ('title', 'author', 'year_published', 'publisher_name')

    def __str__(self):
        return f"{self.title} - {self.author.name}"





