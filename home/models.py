from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Gallery(models.Model):
    imgName = models.CharField(max_length=100)
    imgUrl = models.CharField(max_length=1000)
    imgDesc = models.CharField(max_length=1000)
    imgDate = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='imgName', unique=True)

    def __str__(self):
        return self.imgName
