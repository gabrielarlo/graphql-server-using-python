import strawberry
from .subscriptions import Subscription

schema = strawberry.Schema(subscription=Subscription)
