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
    rating = models.IntegerField(default=0)
    comment = models.TextField(null=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.game.title + " - " + str(self.rating)
    

class comments(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=False)
    comment = models.TextField(null=False)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.user.username + " - " + self.game.title
    
class MissingReview(models.Model):
    game = models.CharField(max_length=50, null=False)
    date = models.DateTimeField(default=timezone.now)
    comment = models.TextField(null=False)
    def __str__(self):
        return self.game + " - " + str(self.date)
    
