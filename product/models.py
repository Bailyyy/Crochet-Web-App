from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):

    CATEGORIES = (
        ('Crochets', 'Crochets'), 
        ('Crochet Bundles', 'Crochet Bundles'),
        ('Donmac', 'Donmac')
    )

    STARS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=25, default="crochets", choices=CATEGORIES)
    quantity = models.IntegerField(default=5)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="products")
    price = models.IntegerField()
    star = models.CharField(max_length=15, default='1', choices=STARS)
    location = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Calculate and set the unit_price when saving the object.
        self.unit_price = self.price * self.quantity
        super(Product, self).save(*args, **kwargs)


    def __str__(self):
        return f"{self.name}-({self.quantity}) by {self.owner}"


