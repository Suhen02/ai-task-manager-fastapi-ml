from app.models.user import User
from app.core.security import hash_password, verify_password, create_token
from app.core.exceptions import BadRequestException

def register_user(db, user):
    db_user = User(email=user.email, password=hash_password(user.password))
    db.add(db_user)
    db.commit()
    return db_user


def login_user(db, user):
    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise BadRequestException("User not found")

    if not verify_password(user.password, db_user.password):
        raise BadRequestException("Invalid credentials")

    return create_token({"id": db_user.id, "role": db_user.role})