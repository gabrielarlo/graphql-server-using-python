import strawberry
from .user_subscriptions import UserSubscription

# Combine all subscriptions into a single Subscription class
@strawberry.type
class Subscription(UserSubscription):
    pass
