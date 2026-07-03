from django.db import models
class bola(models.Model):
    name = models.CharField(max_length=250)
    narxi = models.CharField(max_length=250)
    malumot = models.TextField(max_length=250)
    rasm = models.ImageField(upload_to="bu",null=True,blank=False)

    def __str__(self):
        return f"{self.name}"