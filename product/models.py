from django.db import models
from django.conf import settings
from authentication.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.name

class ProductInCart(models.Model):
    product = models.ManyToManyField(Product)
    quantity = models.PositiveIntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    def calculate_final_price(self):
        total_price = sum(product.price for product in self.product.all())
        return total_price * self.quantity
    