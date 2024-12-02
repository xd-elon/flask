from ariadne import make_executable_schema
from .type_defs import type_defs
from .resolvers import query

graphql_schema = make_executable_schema(type_defs, query)