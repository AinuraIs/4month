from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField(upload_to='product_images/%Y/%m/%d')
    name = models.CharField(max_length=100)
    description = models.TextField()
    rate = models.IntegerField(default=0)
    comments = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(
        Category,
        related_name='products'
    )

    def __str__(self):
        return f'{self.name} - {self.rate}'



class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Review for {self.product.name}'