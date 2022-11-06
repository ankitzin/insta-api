from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.oauth2 import get_current_user
from db.database import get_db
from schemas.post_schema import CommentBase, UserAuth
from services.db_comment import get_all, create

router = APIRouter(
    tags=['comment'],
    prefix='/comment'
)


@router.get('/all/{post_id}')
def comments(post_id: int, db: Session = Depends(get_db)):
    return get_all(db, post_id)


@router.post("")
def create_comment(request: CommentBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return create(db, request)
