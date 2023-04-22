from django.db import models


CATEGORY_CHOICES = (
    ("MEN","MEN"),
    ("WOMEN", "WOMEN"),
    ("GENERAL", "GENERAL")
)
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100)
    image = models.ImageField(upload_to="product_images", default="product.jpg")
    price = models.DecimalField(max_digits=12, decimal_places=2)

    # class meta:
    #     verbose_name_plural = "Products" this is code for changing name of the model displaying on admin panel



    def __str__(self):
        return self.name