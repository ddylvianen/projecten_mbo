from django.db import models
from django.utils import timezone
from compressed_image_field import CompressedImageField

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=50, null=False)
    maker = models.CharField(max_length=50, null=False)
    img = CompressedImageField(null=False, upload_to='profiles', default='default_profile.jpg', quality=80)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f"/game/{self.id}/"

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=False)
    rating = models.IntegerField(min_value=1, max_value=5, default=0)
    comment = models.TextField(null=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.game.title + " - " + str(self.rating)
    

class comments:
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=False)
    comment = models.TextField(null=False)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.game.title + " - " + str(self.comment)
    
class missing_review:
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(default=timezone.now)
    comment = models.TextField(null=False)
    def __str__(self):
        return self.game.title + " - " + str(self.date)