from django.db import models
from category.models import Category
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length = 150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/products')
    num_in_stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name