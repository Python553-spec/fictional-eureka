from django.db import models

class sherbek212(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.name} | {self.last_name}"