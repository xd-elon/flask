from ariadne import QueryType

query = QueryType()

@query.field("hello")
def resolve_hello(_, info):
    return "Hello, GraphQL with Ariadne!"