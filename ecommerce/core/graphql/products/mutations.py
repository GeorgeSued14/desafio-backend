from ariadne import MutationType
from ariadne_jwt.decorators import login_required

from apps.products.models import Product

mutation = MutationType()

@mutation.field('createProduct')
@login_required
def resolve_create_product(self, info, input={}, **kwargs):

    has_product = Product.objects.filter(name=input['name']).first()
    
    if not has_product:

        product = Product(
            name=input['name'],
            price=input['price'],
            quantity=input['quantity']
        )

        if "description" in input.keys():
            product.description = input['description']

        product.save()

        return {
            "ok": True, 
            "product": product
        }

    return {
        "ok": False, 
        "err": "Product with name {} already register".format(has_product.name)
    }
