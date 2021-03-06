from django.db.models import Q

from ariadne import QueryType
from ariadne_jwt.decorators import login_required

from apps.orders.models import Order, OrderProduct
from apps.customers.models import Customer
from apps.products.models import Product



query = QueryType()

@query.field('orders')
@login_required
def resolve_orders(self, info, **kwarg):
    return Order.objects.all()

@query.field('order')
@login_required
def resolve_order(self, info, order_id, **kwarg):

    order = Order.objects.get(pk=order_id)
    customer = Customer.objects.get(pk=order.customer_id.id)
    order_product = OrderProduct.objects.filter(order_id=order.id)
    print(order_product)
    return {
        "ok": True,
        "customer": customer,
        "order": order,
        "items": order_product,
        "err": None
    }