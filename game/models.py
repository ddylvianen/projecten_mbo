from django.db import models
from django.utils import timezone
from compressed_image_field import CompressedImageField

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    img = CompressedImageField(null=True, upload_to='profiles', default='default_profile.jpg', quality=60)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f"/game/{self.id}/"

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rating = models.FloatField()
    comment = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.game.title + " - " + str(self.rating)