from django.db import models

# Create your models here.

# Create your models here.

# news
class news(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    image = models.ImageField(upload_to='photos/%y/%m/%d')



# news
class news(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    image = models.ImageField(upload_to='photos/%y/%m/%d')



