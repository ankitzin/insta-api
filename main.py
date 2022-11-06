from fastapi import FastAPI
from db.database import engine
from models import dbUser
from routers import user_route

app = FastAPI()


app.include_router(user_route.router)

@app.get("/")
def root():
    return "Hello world"


dbUser.Base.metadata.create_all(engine)
