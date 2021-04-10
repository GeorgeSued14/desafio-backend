
from ariadne import MutationType

from apps.customers.models import Customer
from core.utils.decorators import check_email_exists

mutation = MutationType()

@mutation.field('createCustomer')
@check_email_exists
def resolve_create_customer(self, info, input, **kwarg):
    customer = Customer(
        name=input["name"],
        email=input["email"],
    )
    customer.set_password(input["password"])
    customer.save()

    return {"ok": True, "customer": customer}
