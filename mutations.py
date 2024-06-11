import strawberry
from typing import Optional
from sqlalchemy.orm import Session
from models import User as SQLAlchemyUser
from m_types import UserType
from strawberry.types import Info
from datetime import date
from pubsub import pubsub
import logging

logging.basicConfig(level=logging.INFO)

@strawberry.input
class CreateUserInput:
    name: str
    bdate: date

@strawberry.input
class UpdateUserInput:
    id: int
    name: Optional[str] = None
    bdate: Optional[date] = None

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_user(self, info: Info, input: CreateUserInput) -> UserType:
        db: Session = info.context["db"]
        user = SQLAlchemyUser(name=input.name, bdate=input.bdate)
        db.add(user)
        db.commit()
        db.refresh(user)
        logging.info(f"User created: {user}")
        await pubsub.publish("user_created", user)
        await pubsub.publish(f"user_{user.id}_updated", user)
        return UserType(id=user.id, name=user.name, age=UserType.calculate_age(user.bdate))

    @strawberry.mutation
    async def update_user(self, info: Info, input: UpdateUserInput) -> UserType:
        db: Session = info.context["db"]
        user = db.query(SQLAlchemyUser).filter(SQLAlchemyUser.id == input.id).first()
        if input.name:
            user.name = input.name
        if input.bdate:
            user.bdate = input.bdate
        db.commit()
        db.refresh(user)
        logging.info(f"User updated: {user}")
        await pubsub.publish("user_updated", user)
        await pubsub.publish(f"user_{user.id}_updated", user)
        return UserType(id=user.id, name=user.name, age=UserType.calculate_age(user.bdate))
