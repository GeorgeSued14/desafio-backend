from ariadne import QueryType

from apps.customers.models import Customer

query = QueryType()

@query.field('customers')
def resolve_customers(*_):
    return Customer.objects.all()

@query.field('customer')
def resolve_customers(*_, customer_id):
    return Customer.objects.get(pk=customer_id)

