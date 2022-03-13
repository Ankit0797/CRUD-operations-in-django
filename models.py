from django.db import models
from datetime import datetime, date

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    detail=models.TextField()
    
class Emp(models.Model):
    empid=models.CharField(max_length=100)
    detail=models.TextField()
    joindate=models.DateField(auto_now_add=False, auto_now=False)
    
