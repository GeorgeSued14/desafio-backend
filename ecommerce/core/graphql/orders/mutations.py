from ariadne import MutationType

from apps.orders.models import Order, OrderProduct
from apps.customers.models import Customer
from apps.products.models import Product

mutation = MutationType()

@mutation.field('createOrder')
def resolve_create_order(_,info, customer_id, input):
    customer = Customer.objects.get(pk=customer_id)
    order = Order.objects.create(customer_id=customer)

    for order_product in input:
        product = Product.objects.get(pk=order_product['product'])
        order_product = OrderProduct(
            order_id=order,
            product_id=product,
            quantity=order_product['quantity']
        )
        order_product.save() 

    order  

    return {"ok": True, "order": order}
