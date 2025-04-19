from django.db import models
from django.contrib.auth.models import User

class data(models.Model):
    name = models.CharField(max_length=100)




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.user.username
    

class img(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    category=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.title

