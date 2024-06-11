import asyncio
import strawberry
from typing import AsyncGenerator, Optional
from m_types import UserType
from pubsub import pubsub
import logging

logging.basicConfig(level=logging.INFO)

@strawberry.type
class Subscription:
    @strawberry.subscription
    async def user_created(self) -> AsyncGenerator[Optional[UserType], None]:
        queue = await pubsub.subscribe("user_created")
        try:
            while True:
                try:
                    user = await asyncio.wait_for(queue.get(), timeout=10.0)
                    logging.info(f"User created event: {user}")
                    yield UserType(id=user.id, name=user.name, age=UserType.calculate_age(user.bdate))
                except asyncio.TimeoutError:
                    logging.info("No user created event, sending heartbeat")
                    yield None
        finally:
            await pubsub.unsubscribe("user_created", queue)

    @strawberry.subscription
    async def user_updated(self) -> AsyncGenerator[Optional[UserType], None]:
        queue = await pubsub.subscribe("user_updated")
        try:
            while True:
                try:
                    user = await asyncio.wait_for(queue.get(), timeout=10.0)
                    logging.info(f"User updated event: {user}")
                    yield UserType(id=user.id, name=user.name, age=UserType.calculate_age(user.bdate))
                except asyncio.TimeoutError:
                    logging.info("No user updated event, sending heartbeat")
                    yield None
        finally:
            await pubsub.unsubscribe("user_updated", queue)

    @strawberry.subscription
    async def user_specific(self, user_id: int) -> AsyncGenerator[Optional[UserType], None]:
        queue = await pubsub.subscribe(f"user_{user_id}_updated")
        try:
            while True:
                try:
                    user = await asyncio.wait_for(queue.get(), timeout=10.0)
                    logging.info(f"User {user_id} updated event: {user}")
                    yield UserType(id=user.id, name=user.name, age=UserType.calculate_age(user.bdate))
                except asyncio.TimeoutError:
                    logging.info(f"No update for user {user_id}, sending heartbeat")
                    yield None
        finally:
            await pubsub.unsubscribe(f"user_{user_id}_updated", queue)
