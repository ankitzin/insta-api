from fastapi import FastAPI
from db.database import engine
from models import dbUser
from routers import user_route, post_route
from fastapi.staticfiles import StaticFiles
from auth import authentication

app = FastAPI()


app.include_router(user_route.router)
app.include_router(post_route.router)
app.include_router(authentication.router)


@app.get("/")
def root():
    return "Hello world"


dbUser.Base.metadata.create_all(engine)

app.mount('/images', StaticFiles(directory='images'), name='images')
