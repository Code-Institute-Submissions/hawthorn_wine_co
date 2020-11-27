from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Country(models.Model):

    class Meta:
        verbose_name_plural = 'Countries'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.friendly_name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    year = models.CharField(max_length=254, null=True, blank=True)
    producer = models.CharField(max_length=254, null=True, blank=True)
    grapes = models.CharField(max_length=254, null=True, blank=True)
    area = models.CharField(max_length=254, null=True, blank=True)
    country = models.ForeignKey('Country', null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    alcohol_percentage = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    tastes_good_for = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
