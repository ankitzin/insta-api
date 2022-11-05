from fastapi import FastAPI
from db.database import engine
from models import dbUser

app = FastAPI()


@app.get("/")
def root():
    return "Hello world"


dbUser.Base.metadata.create_all(engine)
