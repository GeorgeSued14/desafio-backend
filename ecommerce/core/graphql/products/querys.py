from ariadne import QueryType

from apps.products.models import Product

query = QueryType()

@query.field('products')
def resolve_product(*_):
    return Product.objects.all()

@query.field('product')
def resolve_product(*_, product_id):
    return Product.objects.get(pk=product_id)
