from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
# Create your models here.


class product(models.Model):
    brand= models.ForeignKey(get_user_model(), on_delete=CASCADE)
    name= models.CharField(max_length=64)
    price=models.IntegerField()
    description= models.TextField()
    rating=models.IntegerField()

    def __str__(self):
        return self.name


