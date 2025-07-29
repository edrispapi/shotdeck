from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)  # مثل Genre, Color, Camera, Emotion و ...

    def __str__(self):
        return f'{self.category} - {self.name}'

class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.title} ({self.year})'

class Image(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='images')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image_file = models.ImageField(upload_to='images/')
    tags = models.ManyToManyField(Tag, related_name='images')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
