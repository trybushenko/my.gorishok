from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from apps.product_catalog.models import Product

User = get_user_model()

# Create your models here.
class ShoppingSession(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)  # ForeignKey to User model
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # DecimalField for total
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'shopping_session'
        constraints = [
            models.UniqueConstraint(fields=['id', 'user'], name='session_index')
        ]  # UniqueConstraint for session_index

class OrderDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    payment_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id'], name='order_index'),
            models.UniqueConstraint(fields=['id', 'user_id'], name='customer_order_index'),
        ]

class CartItem(models.Model):
    session = models.ForeignKey(ShoppingSession, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['session', 'product'], name='unique_cart_item')
        ]

    def __str__(self):
        return f"{self.session} - {self.product}"
    
class PaymentDetails(models.Model):
    order = models.ForeignKey(OrderDetails, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment for Order {self.order_id}"
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                name='fk_order_payment',
                fields=['order_id']
            )
        ]

        

class OrderItem(models.Model):
    order = models.ForeignKey(OrderDetails, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id', 'order'], name='order_item_unique')
        ]