from django.db import models
from django.utils.translation import gettext_lazy as _

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
        verbose_name=_('quantity'),
        default=0
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
    
    def remove_unit(self):
        if self.quantity == 0:
            return '{} has no item in stock'.format(self.name)
        quantity=-1
        return quantity