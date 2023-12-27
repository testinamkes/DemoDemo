from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    description=models.TextField()
    year=models.IntegerField()
    cast=models.CharField(max_length=250)


def __str__(self):
    return self.name