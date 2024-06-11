import strawberry

@strawberry.type
class OtherQuery:
    @strawberry.field
    def hello(self) -> str:
        return "Hello, world!"
