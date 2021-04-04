from django.test import TestCase
from django.db.models.query import QuerySet
from .models import Customer

class CustomerModelTest(TestCase):

    @classmethod
    def setUpTestData(self):
        Customer.objects.create(
            name='Joe',
            email='joedoe@email.com',
            password='1234'    
        )
        self.customer = Customer.objects.get(pk=1)
   
    def test_first_name_label(self):
        field_label = self.customer._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'nome')

    def test_first_name_max_length(self):
        max_length = self.customer._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)

    def test_type_return_customer(self):
        customers = Customer.objects.all()
        self.assertEqual(type(customers), QuerySet)

    def test_customer_update(self):
        Customer.objects.filter(pk=1).update(
            name="Doe",
            email="doe@email.com"
        )
        self.assertEqual(self.customer, QuerySet(model=Customer).get(name="Doe"))

    def test_customer_delete(self):
        Customer.objects.filter(pk=1).delete()
        self.assertEqual(None, QuerySet(model=Customer).first())
