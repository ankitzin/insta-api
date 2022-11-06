from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from schemas.user_schema import UserDisplay, UserBase
from services.db_user import create_user

router = APIRouter(
    tags=['user'],
    prefix='/user'
)


@router.post('', response_model=UserDisplay)
def create_user_route(request:UserBase, db: Session = Depends(get_db)):
    return create_user(request, db)
