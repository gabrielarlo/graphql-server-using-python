from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
from database import SessionLocal, database
from queries import Query
from mutations import Mutation, pubsub
from subscriptions import Subscription

schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

graphql_app = GraphQLRouter(
    schema,
    context_getter=lambda: {"db": next(get_db()), "pubsub": pubsub}
)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the GraphQL server"}

app.include_router(graphql_app, prefix="/graphql")

app.dependency_overrides[get_db] = get_db
