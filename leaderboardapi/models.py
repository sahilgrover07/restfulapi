from django.db import models

# Create your models here.
class Leaderboarddetail(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age=models.CharField(max_length=3)
    address = models.CharField(max_length=300)
    points = models.CharField(max_length=3, default=0)
