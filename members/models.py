from django.db import models

# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length=255)
    height = models.FloatField()
    weight = models.FloatField()

    def __str__(self):
        return f"{self.name} h:{self.height} w:{self.weight}"
