from django.db import models
from django.utils.text import slugify
from django.utils import timezone
    
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(default='', null=False)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name}'
    
class Image(models.Model):
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Set created_at when the user is created for the first time
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()  # Update modified_at every time the user is saved
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.image.name
    
class Discount(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Set created_at when the user is created for the first time
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()  # Update modified_at every time the user is saved
        super().save(*args, **kwargs)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(discount_percent__gte=0), name='discount_percent_non_negative')
        ]
        
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    images = models.ManyToManyField(Image, through='ImageAssociation')
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Set created_at when the user is created for the first time
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()  # Update modified_at every time the user is saved
        super().save(*args, **kwargs)
    def __str__(self) -> str:
        return f'{self.category}: {self.name}'
    
class ImageAssociation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.product} - {self.image}'
    