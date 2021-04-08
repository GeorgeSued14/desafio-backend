from ariadne import MutationType

from apps.customers.models import Customer

mutation = MutationType()

@mutation.field('createCustomer')
def resolve_create_customer(_, info, input):
    customer = Customer.objects.create(
        name=input["name"],
        email=input["email"],
    )
    customer.set_password(input["password"])
    customer.save()

    return {"ok": True, "customer": customer}
