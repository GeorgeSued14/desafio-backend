from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from apps.products.models import Product


class Order(models.Model):
    class Meta:
        db_table = "order"
        ordering = ['-created_at']

    id = models.AutoField(
        verbose_name=_('order_id'),
        primary_key=True
    )
    customer_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        verbose_name=_('created_at'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_('updated_at'),
        auto_now=True
    )

    def __str__(self):
        return '{}'.format(self.id)
    
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()
        return total


class OrderProduct(models.Model):
    class Meta:
        db_table = "order_product"
        ordering = ['-created_at']
    
    id = models.AutoField(
        verbose_name=_('order_product_id'),
        primary_key=True
    )
    order_id = models.ForeignKey(
        Order, 
        on_delete=models.CASCADE
    )
    product_id = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(
        verbose_name=_('quantity'),
        default=1
    )
    total = models.FloatField(
        verbose_name=_('item total'),
        default=0
    ) 
    created_at = models.DateTimeField(
        verbose_name=_('created_at'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_('updated_at'),
        auto_now=True
    )
    def __str__(self):
        return '{} <{}>'.format(self.id, self.product_id)

    def get_total_items_price(self):
        return self.quantity * self.product_id.price 
        
        
        
