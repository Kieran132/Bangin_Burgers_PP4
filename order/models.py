from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft", (1, "Published")))


class FoodItem(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='food_images/', blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='food_likes', blank=True)

    def __str__(self):
        return self.name

    def number_of_likes(self):
        return self.likes.count()


