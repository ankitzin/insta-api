from sqlalchemy.orm import Session
from models.dbUser import DbUser
from schemas.user_schema import UserBase


def create_user(user: UserBase, db: Session):
    new_user = DbUser(
        username=user.username,
        email=user.email,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
