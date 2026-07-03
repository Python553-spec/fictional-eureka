from django.db import models
from django.core.validators import FileExtensionValidator
class Product(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False)
    price = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False)
    desciption = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='',blank=True,null=True)
    valiede_mp4 = FileExtensionValidator(['mp4'])
    file = models.FileField(upload_to='vedo/',blank=True,null=True,validators=[valiede_mp4])

    def __str__(self):
        return self.name