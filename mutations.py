import strawberry
from typing import Optional
from sqlalchemy.orm import Session
from models import User as SQLAlchemyUser
from m_types import UserType
from strawberry.types import Info
from datetime import date

@strawberry.input
class CreateUserInput:
    name: str
    bdate: date

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_user(self, info: Info, input: CreateUserInput) -> UserType:
        db: Session = info.context["db"]
        user = SQLAlchemyUser(name=input.name, bdate=input.bdate)
        db.add(user)
        db.commit()
        db.refresh(user)
        return UserType(id=user.id, name=user.name, age=UserType.calculate_age(user.bdate))
