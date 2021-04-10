from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

from core.utils.handle_message import messages

class Product(models.Model):
    class Meta:
        db_table = "product"
        ordering = ['-created_at']

    id = models.AutoField(
        verbose_name=_('product_id'),
        primary_key=True
    )
    name = models.CharField(
        verbose_name=_('product name'),
        max_length=100
    )
    price = models.FloatField(
        verbose_name=_('price'),
    )
    description = models.TextField(
        verbose_name=_('description'),
        null=True
    )
    quantity = models.IntegerField(
        verbose_name=_('stock quantity'),
        default=0,
        validators=[MinValueValidator(0)]
    )
    
    created_at = models.DateTimeField(
        verbose_name=_('created_at'),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_('updated_at'),
        auto_now=True
    )

    def __str__(self):
        return '{} <{}>'.format(self.id, self.name)
    
    @property
    def verify_stock(self):
        if self.quantity > 0:
            return True

    def low_items_stock(self):
        if self.verify_stock:
            if self.quantity <= int(5):
                return '{}. Quantity:{}'.format(
                    messages('low_stock'), 
                    self.quantity
                )
            else:
                return False
        return messages('not_stock')

    def add_items_stock(self, quantity):
        self.quantity = self.quantity + quantity
        self.save()
                
    def get_items_stock(self, quantity):
        if self.verify_stock:
            if quantity > self.quantity:
                return messages('greater_than_stock')
                
            self.quantity = self.quantity - quantity
            self.save()
        
            return quantity
    
        return messages('not_stock')
