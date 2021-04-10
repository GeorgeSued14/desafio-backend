from ariadne import MutationType
from ariadne_jwt.decorators import login_required

from apps.orders.models import Order, OrderProduct
from apps.customers.models import Customer
from apps.products.models import Product

from core.utils.handle_message import messages

mutation = MutationType()

@mutation.field('createOrder')
@login_required
def resolve_create_order(self, info, customer_id, input, **kwarg):

    if not input:
        return {
            "ok": False,
            "order": None,
            "err": 'Input not defined'
        }
    else:
        customer_id = Customer.objects.get(pk=customer_id)
        
        for item in input:
            product_id = item['product']
            quantity = int(item['quantity'])

            product = Product.objects.get(pk=product_id)
            
            if not product.verify_stock:
                return {
                    "ok": False,
                    "msg": messages('not_stock')
                }
            
            elif product.get_items_stock(quantity) != quantity:

                return {
                    "ok": False,
                    "msg": messages('greater_than_stock')
                }

            order = Order.objects.create(customer_id=customer_id)

            order_product = OrderProduct(
                order_id=order,
                product_id=product
            )

            order_product.quantity = quantity
            order_product.total = order_product.get_total_items_price()
            
            order_product.save()

            return {
                "ok": True, 
                "order": order,
                "err": None
            }
