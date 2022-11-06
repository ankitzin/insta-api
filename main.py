from fastapi import FastAPI
from db.database import engine
from models import dbUser
from routers import user_route, post_route, comment_route
from fastapi.staticfiles import StaticFiles
from auth import authentication
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


app.include_router(user_route.router)
app.include_router(post_route.router)
app.include_router(authentication.router)
app.include_router(comment_route.router)


@app.get("/")
def root():
    return "Hello world"

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


dbUser.Base.metadata.create_all(engine)

app.mount('/images', StaticFiles(directory='images'), name='images')
