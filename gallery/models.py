from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=30)

class Location(models.Model):
    location_name = models.CharField(max_length=100) 

    
class Image(models.Model):
    image_name=models.CharField(max_length=50)
    description=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    location=models.ForeignKey(Location,on_delete=models.CASCADE)




