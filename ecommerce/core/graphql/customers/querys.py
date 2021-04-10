from ariadne import QueryType
from ariadne_jwt.decorators import login_required

from apps.customers.models import Customer

query = QueryType()

@query.field('customers')
def resolve_customers(self, info, **kwargs):
    return Customer.objects.all()

@query.field('customer')
def resolve_customers(self, info, customer_id, **kwarg):
    return Customer.objects.get(pk=customer_id)

