from django.db import models
from django.conf import settings
import random

User = settings.AUTH_USER_MODEL        # auth.user
TAG_MODEL_VALUES = ['GPU', 'CPU', 'Storage']

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    public = models.BooleanField(default=True)


    @property
    def sale_price(self):
        # 25% discount for product's price
        return f'{float(self.price) * 0.75 :.2f}'

    

    def is_public(self):
        return self.public

    def get_tags_list(self):
        return [random.choice(TAG_MODEL_VALUES)]