from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.dbUser import DbUser
from schemas.user_schema import UserBase
from models.hashing import Hash


def create_user(user: UserBase, db: Session):
    new_user = DbUser(
        username=user.username,
        email=user.email,
        password=Hash.bcrypt(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with username {user.username} not found.')
    return user
