
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.extensions import db

class User(db.Model):
    __tablename__ = 'users'  # needed, otherwise it would generate a table "user" (lowercase of class name).
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()
    #email: Mapped[str]