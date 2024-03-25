from django.db import models
    
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name}'
    
class Image(models.Model):
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self) -> str:
        return self.image.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    images = models.ManyToManyField(Image, through='ImageAssociation')

    def __str__(self) -> str:
        return f'{self.category}: {self.name}'
    
class ImageAssociation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.product} - {self.image}'