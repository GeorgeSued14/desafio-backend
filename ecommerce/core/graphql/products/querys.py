from ariadne import QueryType
from ariadne_jwt.decorators import login_required

from apps.products.models import Product

query = QueryType()

@query.field('products')
@login_required
def resolve_product(self, info, **kwarg):
    return Product.objects.all()

@query.field('product')
@login_required
def resolve_product(self, info, product_id, **kwarg):
    return Product.objects.get(pk=product_id)
