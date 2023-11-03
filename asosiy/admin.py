from django.contrib import admin
from .models import *

@admin.register(Suv)
class SuvAdmin(admin.ModelAdmin):
    list_display = ['brend', 'narx', 'litr', 'batafsil']

@admin.register(Mijoz)
class MijozAdmin(admin.ModelAdmin):
    list_display = ['ism', 'tel', 'manzil', 'user']
    # list_display = ['ism', 'tel', 'manzil', 'qarz', 'user']

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ['ism', 'yosh', 'ish_vaqti', 'user']

@admin.register(Haydovchi)
class HaydovchiAdmin(admin.ModelAdmin):
    list_display = ['ism', 'tel', 'kiritilgan_sana']

@admin.register(Buyurtma)
class BuyurtmaAdmin(admin.ModelAdmin):
    list_display = ['suv', 'mijoz', 'miqdori', 'umumiy_narxi', 'qabul_qilgan_admin', 'yetkazib_berish_yuklatilgan_haydovchi']
