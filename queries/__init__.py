import strawberry
from queries.other_queries import OtherQuery
from .user_queries import UserQuery

# Combine all queries into a single Query class
@strawberry.type
class Query(UserQuery, OtherQuery):
    pass
