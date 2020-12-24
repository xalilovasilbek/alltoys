from django.db import models


class Market(models.Model):
    name = models.CharField(max_length=50)
    address = models.ForeignKey('Manzil', on_delete=models.CASCADE)
    type = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Manzil(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.city} shahri {self.street} ko'chasi"
