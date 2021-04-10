from apps.customers.models import Customer

def check_email_exists(f):
    def decorated(self, info, input, **kwargs):
        customer = Customer.objects.filter(email=input['email']).exists()
        print("To no decorator %s" % (customer))
        if customer:
            return {
                "ok": False,
                "customer": None,
                "err": "Email already exists"
            }
        return f(self, info, input, **kwargs)
    return decorated