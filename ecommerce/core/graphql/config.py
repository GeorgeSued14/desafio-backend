from ariadne import make_executable_schema, load_schema_from_path

from core.graphql import customers as customers
from core.graphql import products as products
from core.graphql import orders as orders

from core.graphql.scalar import datetime_scalar

type_defs = [
    load_schema_from_path("core/graphql/schema.graphql"),
    load_schema_from_path('core/graphql/customers/schema.graphql'),
    load_schema_from_path('core/graphql/orders/schema.graphql'),
    load_schema_from_path('core/graphql/products/schema.graphql')
]


schema =  make_executable_schema(type_defs, [
    customers.mutation, customers.query, 
    products.mutation, products.query, 
    orders.mutation, orders.query, 
    datetime_scalar
])    
