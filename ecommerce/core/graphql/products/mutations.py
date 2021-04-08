from ariadne import MutationType

from apps.products.models import Product

mutation = MutationType()

@mutation.field('createProduct')
def resolve_create_product(_, info, input):

    has_product = Product.objects.filter(name=input['name']).first()
    
    if not has_product:

        product = Product(
            name=input['name'],
            price=input['price'],
        )

        if 'description' in input.values():
            product.description = input['description']
    
        if 'quantity' in input.values():
            product.quantity = input['quantity']
    
        product.save()

        return {
            "ok": True, 
            "product": product
        }
    
    
    return {
        "ok": False, 
        "err": "Product with name {} already register".format(has_product.name)
    }
