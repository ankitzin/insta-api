import datetime

from sqlalchemy.orm import Session

from schemas.post_schema import PostBase
from models.dbUser import DbPost


def create(db: Session, request:PostBase):
    new_post = DbPost(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        timestamp=datetime.datetime.now(),
        user_id=request.creator_id
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


def get_posts_all(db: Session):
    return db.query(DbPost).all()
