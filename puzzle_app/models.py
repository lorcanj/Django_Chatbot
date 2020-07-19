from django.db import models

# Create your models here.
class Puzzle(models.Model):
    description = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
    # need to check as want the difficulty to be an enum

    def __str__(self):
        return f"{self.description}: {self.text}"
