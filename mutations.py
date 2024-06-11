import strawberry
from mutations import Mutation

schema = strawberry.Schema(mutation=Mutation)

