from typing import List
import strawberry
from sqlalchemy.orm import Session
from models import User as SQLAlchemyUser
from m_types import UserType
from strawberry.types import Info

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello, world!"

    @strawberry.field
    async def users(self, info: Info) -> List[UserType]:
        db: Session = info.context["db"]
        users = db.query(SQLAlchemyUser).all()
        return [
            UserType(
                id=user.id,
                name=user.name,
                age=UserType.calculate_age(user.bdate)
            ) for user in users
        ]
