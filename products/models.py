from django.db import models

class Product(models.Model):
    company_name = models.CharField(max_length=255)
    part_number = models.CharField(max_length=255, unique=True)
    car_model = models.CharField(max_length=255)
    description = models.TextField()
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.final_price = self.mrp - (self.mrp * self.discount / 100)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.company_name} - {self.part_number}"
