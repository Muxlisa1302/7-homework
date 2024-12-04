from django.db import models


class Car(models.Model):
    name=models.CharField(max_length=100)
    model=models.TextField()
    year=models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.model} ({self.year})"
