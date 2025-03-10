from django.db import models
from django.conf import settings


class Recipe(models.Model):
    """Recipe object"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    time_minutes = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.CharField(max_length=255, blank=True)
    # ingredients = models.ManyToManyField('Ingredient')
    # tags = models.ManyToManyField('Tag')
    # image = models.ImageField(null=True, upload_to=recipe_image_file_path)

    def __str__(self):
        return self.title
