from django.db import models

# fields for product name, image, description and price.
class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name
