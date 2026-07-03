# from django.db import models

# class Sherbek(models.Model):
#     name = models.CharField(max_length=100,verbose_name="Ismi")
#     age = models.IntegerField(verbose_name="Yoshi")
#     breed = models.CharField(max_length=100,verbose_name="Nomi")
#     phone = models.CharField(max_length=100,verbose_name="Telefon raqami")
#     gender = models.CharField(max_length=100,verbose_name="Jinsi")
#     email = models.EmailField(null=True, blank=True,verbose_name="Elektron pochta")
#     phone = models.CharField(max_length=100,verbose_name="Kodli hudud",null=True, blank=True)

#     class Meta:
#         verbose_name = "Sherbek"
#         verbose_name_plural = "Sherbek"

#     def __str__(self):
#         return self.name



# from django.db import models

# class Sherbek(models.Model):
#     GENDER_CHOICES = [
#         ('M', 'Erkak'),
#         ('F', 'Ayol'),
#     ]

#     name = models.CharField(max_length=100)
#     age = models.PositiveIntegerField(default=0) 
#     breed = models.CharField(max_length=100, default="")
#     phone = models.CharField(max_length=20, default="")
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
#     email = models.EmailField(null=True, blank=True)
#     Malumot = models.TextField(max_length=300,null=True,blank=True)
#     class Meta:
#         verbose_name = "Sherbek"
#         verbose_name_plural = "Sherbek"

#     def __str__(self):
#         return self.name



from django.db import models
from django.contrib.auth.models import User
# class Conter(models.Model):
#     Gender_Choices = [
#         {'E','Erkak'},
#         ('f','Ayol'),
#     ]

#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     ismi = models.CharField(max_length=46)
#     familya = models.CharField(max_length=45)
#     raqam = models.CharField(max_length=400,null=True,blank=True)
#     yoshi = models.CharField(max_length=300,null=True,blank=True)
#     stem_username = models.CharField(max_length=500)
#     telegram_username = models.CharField(max_length=400,null=True,blank=True)
    

    
#     def __str__(self):
#         return f"{self.ismi} | {self.familya}"


# from django.db import models

# class Sherbek(models.Model):
#     name = models.CharField(max_length=100)
#     surname = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.name} {self.surname}"



from django.db import models

class Ishchi(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    img = models.ImageField(upload_to="rasm")

    def __str__(self):
        return f"{self.name}"