from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL        # auth.user

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)

    @property
    def sale_price(self):
        # 25% discount for product's price
        return f'{float(self.price) * 0.75 :.2f}'