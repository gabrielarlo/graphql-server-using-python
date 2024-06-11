import strawberry
from .user_mutations import UserMutation

# Combine all mutations into a single Mutation class
@strawberry.type
class Mutation(UserMutation):
    pass
