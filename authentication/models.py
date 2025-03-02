from django.db import models
from django.contrib.auth.models import User
import os


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wname = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    gender = models.CharField(max_length=10)
    contact_num = models.FloatField()
    profile_picture = models.ImageField(upload_to='profile_pictures', default='default-profile.jpg')
    def __str__(self):
        return self.wname
    class Meta:
        ordering = ['wname']

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    oname = models.CharField(max_length=40)
    email = models.EmailField(max_length=30)
    gender = models.CharField(max_length=10)
    contact_num = models.FloatField()
    def __str__(self):
        return self.oname
    class Meta:
        ordering = ['oname']

class Product(models.Model):
    company_name = models.CharField(max_length=255,default='',blank=False)
    part_number = models.CharField(max_length=255,default='', blank=True, null=True)
    car_model = models.CharField(max_length=255,default='', blank=True, null=True)
    description = models.TextField(default='', blank=False, null=True)
    mrp = models.DecimalField(max_digits=10, decimal_places=2,blank=False)
    discount = models.DecimalField(max_digits=5, decimal_places=2,default=0,blank=True)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        if self.discount is None:
            self.discount = 0  # Ensure discount is 0 if None
        self.final_price = self.mrp - (self.mrp * self.discount / 100)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.company_name} - {self.part_number}"
