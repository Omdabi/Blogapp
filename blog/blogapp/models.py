from django.db import models

# Create your models here.
class blog(models.Model):
    photo = models.ImageField(upload_to='image')
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=10000)
    