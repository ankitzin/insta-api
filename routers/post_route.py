import random
import shutil
import string
from typing import List

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, status
from sqlalchemy.orm import Session


from auth.oauth2 import get_current_user
from db.database import get_db
from schemas.post_schema import PostDisplay, PostBase, UserAuth
from services.db_post import create, get_posts_all

router = APIRouter(
    tags=['post'],
    prefix='/post'
)

image_url_types = ['absolute', 'relative']


@router.post('', response_model=PostDisplay)
def create_post(request: PostBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    if request.image_url_type not in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='Parameter image can ony take values absolute or relative.')
    return create(db, request)


@router.get("", response_model=List[PostDisplay])
def get_all(db: Session = Depends(get_db)):
    return get_posts_all(db)


@router.post('/image')
def upload_image_route(image: UploadFile = File(...), current_user: UserAuth = Depends(get_current_user)):
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for i in range(6))
    new = f'_{rand_str}.'
    filename = new.join(image.filename.rsplit('.', 1))
    print(filename)
    path = f'images/{filename}'

    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {'filename': path}

