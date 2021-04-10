from ariadne import make_executable_schema, load_schema_from_path, MutationType
from ariadne_jwt import resolve_verify, resolve_refresh, jwt_schema, GenericScalar

from core.graphql import customers as customers
from core.graphql import products as products
from core.graphql import orders as orders

from core.graphql.scalar import datetime_scalar

from .jwt import resolve_token_auth, extended_type_defs

mutation_jwt = MutationType()

mutation_jwt.set_field('verifyToken', resolve_verify)
mutation_jwt.set_field('refreshToken', resolve_refresh)
mutation_jwt.set_field('tokenAuth', resolve_token_auth)

type_defs = [
    load_schema_from_path("core/graphql/schema.graphql"),
    load_schema_from_path('core/graphql/customers/schema.graphql'),
    load_schema_from_path('core/graphql/orders/schema.graphql'),
    load_schema_from_path('core/graphql/products/schema.graphql'),
    jwt_schema,
    extended_type_defs
]

schema = make_executable_schema(type_defs, [mutation_jwt, customers.mutation, customers.query, orders.mutation, orders.query, products.mutation, products.query, datetime_scalar, GenericScalar]
)    


