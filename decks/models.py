from django.db import models

class Deck(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    owner_id = models.IntegerField()  # ID کاربر مالک (آیدی از سرویس کاربران)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class DeckImage(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='deck_images')
    image_id = models.IntegerField()  # آیدی تصویر (از سرویس Image)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('deck', 'image_id')
        ordering = ['sort_order']

class DeckShare(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='shares')
    user_id = models.IntegerField()  # آیدی کاربر گیرنده
    permission = models.CharField(max_length=10, choices=[('view', 'View'), ('edit', 'Edit')], default='view')
    invited_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('deck', 'user_id')
