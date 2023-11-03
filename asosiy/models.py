from django.db import models
from django.contrib.auth.models import User

class Suv(models.Model):
    brend = models.CharField(max_length=100)
    narx = models.FloatField()
    litr = models.IntegerField()
    batafsil = models.TextField()

class Mijoz(models.Model):
    ism = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    manzil = models.TextField()
    garz = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Admin(models.Model):
    ism = models.CharField(max_length=100)
    yosh = models.IntegerField()
    ish_vaqti = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Haydovchi(models.Model):
    ism = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    kiritilgan_sana = models.DateField()

class Buyurtma(models.Model):
    suv = models.ForeignKey(Suv, on_delete=models.CASCADE)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    miqdori = models.IntegerField()
    umumiy_narxi = models.FloatField()
    qabul_qilgan_admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    yetkazib_berish_yuklatilgan_haydovchi = models.ForeignKey(Haydovchi, on_delete=models.CASCADE)

























# from django.db import models
# from django.contrib.auth.models import User
#
# class Suv(models.Model):
#     brend = models.CharField(max_length=30)
#     narx = models.CharField(max_length=30)
#     litr = models.PositiveIntegerField()
#     batafsil = models.TextField()
#
#     def __str__(self):
#         return self.brend
#
# class Mijoz(models.Model):
#     ism = models.CharField(max_length=50)
#     tel = models.CharField(max_length=20)
#     manzil = models.CharField(max_length=100)
#     qarz = models.CharField(max_length=50)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.ism
#
# class Admin(models.Model):
#     ism = models.CharField(max_length=50)
#     yosh = models.PositiveIntegerField()
#     ish_vaqti = models.CharField(max_length=50)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.ism
#
# class Haydovchi(models.Model):
#     ism = models.CharField(max_length=50)
#     tel = models.CharField(max_length=20)
#     kiritilgan_sana = models.DateField()
#
#     def __str__(self):
#         return self.ism
#
# class Buyurtma(models.Model):
#     suv = models.ForeignKey(Suv, on_delete=models.CASCADE)
#     qachon = models.DateField()
#     mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
#     miqdor = models.CharField(max_length=50)
#     umumiy_narxi = models.CharField()
#     admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
#     haydovchi = models.ForeignKey(Haydovchi, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.suv