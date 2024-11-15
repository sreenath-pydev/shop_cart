from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class Product(models.Model):
    # Predefined categories for product classification
    CATEGORY_CHOICES = [
        ('men', 'Men'),
        ('women', 'Women'),
    ]
    
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.CharField(
        max_length=5,  
        choices=CATEGORY_CHOICES,
        default='men',  
    )

    def get_absolute_url(self):
        return reverse('product_list')

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.quantity * self.product.price
STATE_CHOICES = [
    ('kerala', 'Kerala'),
    ('karnataka', 'Karnataka'),
    ('andhra', 'Andhra Pradesh'),
]
class UserAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100 )
    place = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(
        max_length=15,  
        choices=STATE_CHOICES,
        default=' ',
        blank=True, null=True  
    )
    pincode = models.CharField(max_length=6 , blank=True, null=True)

