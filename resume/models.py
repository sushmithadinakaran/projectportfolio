from django.db import models

# Create your models here.
class details(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField()
    message=models.TextField()
    phone_no=models.CharField(max_length=15)
